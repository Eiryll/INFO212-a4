from project import app
from project.models.Customer import find_customer_by_id, find_all_customers, delete_customer_by_id, \
    update_customer, _create_customer
from flask import request


@app.get('/customers')
def get_customers():
    customers = find_all_customers()

    data = [{"name": c.name, "age": c.age} for c in customers]

    return data


@app.post('/customers')
def create_customer():
    body = request.get_json()

    _create_customer(body)

    return {}


@app.get("/customers/<id>")
def get_by_id(id):
    customer = find_customer_by_id(int(id))

    if customer is None:
        return {}

    return {"name": customer.name, "age": customer.age}


@app.put("/customers/<id>")
def update(id):
    body = request.get_json()

    update_customer(int(id), body)

    return {}


@app.delete("/customers/<id>")
def delete_by_id(id):
    delete_customer_by_id(int(id))

    return {}
