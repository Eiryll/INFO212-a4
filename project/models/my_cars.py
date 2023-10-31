from .common import _get_connection, get_nodes, get_node, node_to_json


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


def save_car(make, model, reg, year, capacity):
    cars = _get_connection().execute_query(
        "MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity}) RETURN a;", make=make,
        model=model, reg=reg, year=year, capacity=capacity)

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
