import json

from project import app
from flask import render_template, request, redirect, url_for
from project.models.my_cars import *


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
