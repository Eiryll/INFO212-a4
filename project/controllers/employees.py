import json
from project import app
from flask import request

from project.models.Employee import _create_employee, _find_all_employees, _find_employee_by_id, _update_employee, \
    _delete_employee_by_id


@app.get('/employees')
def get_employees():
    return _find_all_employees()


@app.post('/employees')
def create_employee():
    body = json.loads(request.data)

    id = body["id"]
    name = body["name"]
    address = body["address"]
    branch = body["branch"]

    employee_json = _create_employee(id, name, address, branch)

    return employee_json, 200


@app.get("/employees/<id>")
def get_employee_by_id(id):
    return _find_employee_by_id(int(id))


@app.put("/employees/<id>")
def update_employee(id):
    body = json.loads(request.data)

    branch = body["branch"]

    employee_json = _update_employee(int(id), branch)

    return employee_json, 200


@app.delete("/employees/<id>")
def delete_employee_by_id(id):
    _delete_employee_by_id(int(id))

    return "", 200

