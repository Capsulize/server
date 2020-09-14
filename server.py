from flask import Flask
from flask import request

app = Flask(__name__)

companies = []
employees = []


@app.route('/<company_name>', methods=["POST"])
def set_company(company_name):
    company = request.get_json()
    print('Received new company:{}, {}'.format(company_name, company))

    if not all(keys in company for keys in ("rooms", "shifts")):
        print("[Company] don't have all keys")
        return {"success": False}

    companies.append(company)

    return {"success": True}


@app.route('/<company_name>', methods=["POST"])
def add_employee(company_name):
    employee = request.get_json()
    print('Received new employee:{}, {}'.format(company_name, employee))

    if not all(keys in employee for keys in ("home_location", "car_capacity", "dependencies", "shifts_availability")):
        print("[employee] don't have all keys")
        return {"success": False}

    employee["company_name"] = company_name
    companies.append(employee)

    return {"success": True}


@app.route('/<company_name>', methods=["POST"])
def get_company_data(company_name):
    rooms = companies[company_name]["rooms"]
    shifts = companies[company_name]["shifts"]
    return {"rooms": rooms, "shifts": shifts}


if __name__ == '__main__':
    app.run(port=5555, debug=True)
