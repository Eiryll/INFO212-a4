import json

from project import app
from flask import render_template, request, redirect, url_for, make_response, jsonify
from project.models.Car import *
from project.models.Car import _order_car, _cancel_order_car, _rent_car, _return_car


@app.route('/get_cars', methods=['GET'])
def query_records():
    return findAllCars()


@app.route('/get_car_by_reg_number', methods=["POST"])
def find_car_by_reg_number():
    record = json.loads(request.data)
    print(record)
    print(record["reg"])
    return findCarByReg(record["reg"])


@app.route("/save_car", methods=["POST"])
def save_car_info():
    record = json.loads(request.data)
    print(record)
    return save_car(record["make"], record["model"], record["reg"], record["year"], record["capacity"])


@app.route("/update_car", methods=["PUT"])
def update_car_info():
    record = json.loads(request.data)
    print(record)
    return update_car(record["make"], record["model"], record["reg"], record["year"], record["capacity"])


@app.route("/delete_car", methods=["DELETE"])
def delete_car_info():
    record = json.loads(request.data)
    print(record)
    delete_car(record["reg"])
    return findAllCars()


@app.post("/order_car")
def order_car():
    body = json.loads(request.data)
    customer_id = body["customerId"]
    car_id = body["carId"]

    success, message = _order_car(customer_id, car_id)

    if not success:
        return make_response(jsonify({'error': 'Bad Request', 'message': message}), 400)

    return "", 200


@app.post("/cancel_order_car")
def cancel_order_car():
    body = json.loads(request.data)
    customer_id = body["customerId"]
    car_id = body["carId"]

    success, message = _cancel_order_car(customer_id, car_id)

    if not success:
        return make_response(jsonify({'error': 'Bad Request', 'message': message}), 400)

    return "", 200


@app.post("/rent_car")
def rent_car():
    body = json.loads(request.data)
    customer_id = body["customerId"]
    car_id = body["carId"]

    success, message = _rent_car(customer_id, car_id)

    if not success:
        return make_response(jsonify({'error': 'Bad Request', 'message': message}), 400)

    return "", 200


@app.post("/return_car")
def return_car():
    body = json.loads(request.data)
    customer_id = body["customerId"]
    car_id = body["carId"]
    damage_status = body["status"]

    success, message = _return_car(customer_id, car_id, damage_status)

    if not success:
        return make_response(jsonify({'error': 'Bad Request', 'message': message}), 400)

    return "", 200
