from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver
import json
URI = "bolt://localhost:7687/neo4j"
AUTH = ("neo4j", "password1234")
def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver
def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties
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
    cars = _get_connection().execute_query("MERGE (a:Car{make: $make, model: $model, reg: $reg, year: $year, capacity:$capacity}) RETURN a;", make = make, model = model, reg = reg, year = year, capacity = capacity)
    nodes_json = [node_to_json(record["a"]) for record in cars]
    print(nodes_json)
    return nodes_json


def delete_car(reg):
    _get_connection().execute_query("MATCH (a:Car{reg: $reg}) delete a;", reg =
reg)

# Cars added to the sytem for testing

save_car("Ford", "Focus", "11D1234", 2011, 5)
save_car("Nissan", "Micra", "12D1234", 2012, 5)
save_car("Toyota", "Yaris", "13D1234", 2013, 5)
save_car("Ford", "Fiesta", "14D1234", 2014, 5)
save_car("Volkswagen", "Golf", "15D1234", 2015, 5)
save_car("Volkswagen", "Polo", "16D1234", 2016, 5)
save_car("Toyota", "Corolla", "17D1234", 2017, 5)