from neo4j import GraphDatabase, Driver, AsyncGraphDatabase, AsyncDriver

URI = "bolt://localhost:7687/neo4j"
AUTH = ("neo4j", "password1234")


def _get_connection() -> Driver:
    driver = GraphDatabase.driver(URI, auth=AUTH)
    driver.verify_connectivity()
    return driver


def has_records(data):
    """Check if data result has any records within in (data)"""
    return len(data[0]) > 0


def get_node(data):
    """Returns a single node in the dataset. For when there is only a single record out."""
    return data[0][0][0]


def get_nodes(data):
    """Returns an iterable (multiple) of the innermost nodes in the dataset"""
    return map(lambda r: r[0], data[0])


def node_to_json(node):
    node_properties = dict(node.items())
    return node_properties
