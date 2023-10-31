from project.models.common import _get_connection, has_records, get_nodes, get_node, node_to_json


def _find_all_employees():
    data = _get_connection().execute_query("MATCH (e:Employee) RETURN e;")

    nodes = get_nodes(data)
    node_jsons = [node_to_json(node) for node in nodes]

    return node_jsons


def _find_employee_by_id(id):
    data = _get_connection().execute_query("MATCH (e:Employee{id:$id}) RETURN e;", id=id)

    node = get_node(data)
    node_json = node_to_json(node)

    return node_json


def _delete_employee_by_id(id):
    _get_connection().execute_query("MATCH (e:Employee{id:$id}) DELETE e", id=id)


def _create_employee(id, name, address, branch):
    # Create employee
    employee_data = _get_connection().execute_query(
        "CREATE (e:Employee {id:$id, name:$name, branch:$branch, address:$address}) RETURN e",
        id=id,
        name=name,
        branch=branch,
        address=address,
    )

    node = get_node(employee_data)
    node_json = node_to_json(node)

    return node_json


def _update_employee(id, branch):
    # Update employee's branch
    employee_data = _get_connection().execute_query("MATCH (e:Employee{id:$id}) SET e.branch = $branch RETURN e",
                                                    id=id,
                                                    branch=branch,
                                                    )

    node = get_node(employee_data)
    node_json = node_to_json(node)

    return node_json
