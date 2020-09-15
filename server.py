from flask import Flask
from flask import request
from pprint import pprint
from flask import jsonify
from contrib.Algorithm.algorithm.algorithm import *
from contrib.Algorithm.algorithm.input_models import *
from flask_cors import CORS
from random_data import *
app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"`origins`": ["*"]}})

# For now the DSB is this :)
companies = {}
index = 0


@app.route('/<company_name>', methods=["POST"])
def set_company(company_name):
    company = request.get_json()
    print('Received new company:{}, {}'.format(company_name, company))

    if not all(keys in company for keys in ("rooms", "shifts")):
        print("[Company] don't have all keys")
        return {"success": False}

    companies[company_name] = company
    print( companies[company_name])
    return {"success": True}


@app.route('/<company_name>/employee', methods=["POST"])
def add_employee(company_name):
    global index
    employee = request.get_json()
    print('Received new employee:{}, {}'.format(company_name, employee))

    if not all(keys in employee for keys in ("name", "room_id", "car_capacity", "home_location", "shift_dependencies",
                                             "capsule_dependencies", "shift_availability")):
        print("[employee] don't have all keys")
        return {"success": False}

    employee["id"] = str(index)
    index += 1

    companies[company_name]["employees"].append(employee)
    return {"success": True}


@app.route('/<company_name>/capsulize', methods=["POST"])
def capsulize_company(company_name):
    employees = []
    employees_json = companies[company_name]["employees"]
    for i, employee in enumerate(employees_json):
        employees.append(Employee(
            identifier=i,
            room_id=employee["room_id"],
            home_location=employee["home_location"],
            car_capacity=employee["car_capacity"],
            shift_dependencies=set(employee["shift_dependencies"]),
            capsule_dependencies=set(employee["capsule_dependencies"]),
            shift_availability=set(employee["shift_availability"])))

    workspaces = []
    workspaces_json = companies[company_name]["rooms"]
    for i, room in enumerate(workspaces_json):
        workspaces.append(Workspace(
            identifier=i,
            capacity=room["capacity"]
        ))

    return_data = capsulize(len(companies[company_name]["shifts"]), 0.1, employees, workspaces)

    print("input")
    pprint(companies[company_name])
    print("output")
    pprint(return_data)

    return {"success": True}


@app.route('/<company_name>/data', methods=["GET"])
def get_company_data(company_name):
    print(companies)
    rooms = companies[company_name]["rooms"]
    shifts = companies[company_name]["shifts"]

    return {"rooms": rooms, "shifts": shifts}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)
