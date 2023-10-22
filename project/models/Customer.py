from project.models.common import _get_connection, has_records, get_nodes, get_node


def find_all_customers():
    data = _get_connection().execute_query("MATCH (a:Customer) RETURN a;")

    if has_records(data):
        customers = []
        for node in get_nodes(data):
            customer = Customer(node['id'], node['name'], node['age'], node['address'])
            customers.append(customer)
        return customers
    else:
        return None


def find_customer_by_id(id):
    data = _get_connection().execute_query("MATCH (a:Customer) where a.id = $id RETURN a;", id=id)
    if has_records(data):
        node = get_node(data)
        customer = Customer(id, node['name'], node['age'], node['address'])
        return customer
    else:
        return None

def delete_customer_by_id(id):
    _get_connection().execute_query("MATCH (a:Customer) where a.id = $id DELETE a", id=id)



def create_customer(body):
    # Create customer
    _get_connection().execute_query("CREATE (a:Customer {id:$id, name:$name, age:$age, address:$address})",
                                    id=body["id"],
                                    name=body["name"],
                                    age=body["age"],
                                    address=body["address"],
                                    )



def update_customer(id, body):

    # Update customer

    _get_connection().execute_query("MATCH (a: Customer) where a.id = $id SET a.name = $name RETURN a",
                                    id=id,
                                    name=body["name"]
                                    )



class Customer:
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
