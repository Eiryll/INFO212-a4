from .common import _get_connection, get_nodes, get_node, node_to_json, has_records


def findAllCars():
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) RETURN a;")
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json


def findCarByReg(reg):
    with _get_connection().session() as session:
        cars = session.run("MATCH (a:Car) where a.reg=$reg RETURN a;", reg=reg)
        print(cars)
        nodes_json = [node_to_json(record["a"]) for record in cars]
        print(nodes_json)
        return nodes_json


def save_car(make, model, reg, year, capacity, id, status):
    cars = _get_connection().execute_query(
        "MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity, id:$id, status:$status}) RETURN a;",
        make=make,
        model=model, reg=reg, year=year, capacity=capacity, id=id, status=status)

    node = get_node(cars)
    node_json = node_to_json(node)
    print(node_json)
    return node_json


def update_car(make, model, reg, year, capacity):
    car = _get_connection().execute_query(
        "MATCH (a:Car{reg:$reg}) SET a.make = $make, a.model = $model, a.year = $year, a.capacity = $capacity RETURN a;",
        make=make,
        model=model,
        reg=reg,
        year=year,
        capacity=capacity)

    node = get_node(car)
    node_json = node_to_json(node)
    print(node_json)
    return node_json


def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg=
    reg)


def _order_car(customerId, carId):
    # check that the customer has not booked other cars
    customer_data = _get_connection().execute_query(
        "MATCH (cust:Customer{id: $id}) WHERE NOT (cust)-[:Ordered]->() RETURN cust",
        id=customerId)

    if not has_records(customer_data):
        return False, "Customer already have ordered cars"

    # check that car is not already booked
    car_data = _get_connection().execute_query(
        "MATCH (car:Car{id: $id, status:'available'}) WHERE NOT ()-[:Ordered]->(car) RETURN car",
        id=carId)

    if not has_records(car_data):
        return False, "Car is already booked"

    # book the car
    _get_connection().execute_query(
        "MATCH (cust:Customer{id: $customerId}), (car:Car{id: $carId}) CREATE (cust)-[:Ordered]->(car) SET car.status = 'booked'",
        customerId=customerId,
        carId=carId)

    return True, None


def _cancel_order_car(customerId, carId):
    # match the order, and delete if exists. If nothing returned, the order never existed, and we should return an error.
    customer_data = _get_connection().execute_query(
        "MATCH (cust:Customer{id: $customerId})-[o:Ordered]-(car:Car{ id: $carId, status: 'booked'}) DELETE o SET car.status='available' RETURN cust",
        customerId=customerId, carId=carId)

    if not has_records(customer_data):
        return False, "Customer has not booked car, cannot cancel booking"

    return True, None


def _rent_car(customerId, carId):
    rent_data = _get_connection().execute_query(
        "MATCH (cust:Customer{id: $customerId})-[o:Ordered]-(car:Car{ id: $carId}) SET car.status='rented' RETURN cust",
        customerId=customerId, carId=carId)

    if not has_records(rent_data):
        return False, "Customer does not exist, car does not exist, or customer has not booked car"

    return True, None


def _return_car(customerId, carId, damage_status):
    new_status = "available"

    if damage_status == "damaged":
        new_status = "damaged"

    return_data = _get_connection().execute_query(
        "MATCH (cust:Customer{id: $customerId})-[o:Ordered]-(car:Car{ id: $carId, status:'rented'}) SET car.status=$status DELETE o RETURN cust",
        customerId=customerId, carId=carId, status=new_status)

    if not has_records(return_data):
        return False, "Customer does not exist, car does not exist, or car is not rented"

    return True, None
