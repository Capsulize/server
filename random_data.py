import random

from flask import jsonify
from contrib.Algorithm.algorithm.algorithm import *
from contrib.Algorithm.algorithm.input_models import *

# For now the DB is this :)
companies = {}
index = 0

companies["aa"] = {
        "rooms": [],
        "shifts": ["09:00 - 15:00", "16:00 - 23:00"],
        "employees": []
}


names = [
"Muhammad",
"Oliver",
"Jack",
"Noah",
"Jacob",
"Harry",
"Charlie",
"Ethan",
"James",
"Thomas",
"Joshua",
"George",
"William",
"Daniel",
"Leo",
"Ryan",
"Alexander",
"Henry",
"Max",
"Oscar",
"Logan",
"Alfie",
"Adam",
"Lucas",
"Freddie",
"Isaac",
"Aiden",
"Finley",
"Dylan",
"Joseph",
"Liam",
"Theo",
"Samuel",
"Benjamin",
"Archie",
"Jayden",
"Harrison",
"Nathan",
"Michael",
"Mason",
"Sebastian",
"Jackson",
"Jake",
"Luke",
"Edward",
"Zachary",
"Alex",
"Elijah",
"Lewis",
"David",
"Matthew",
"Teddy",
"Elliot",
"Toby",
"Arthur",
"Connor",
"Reuben",
"Caleb",
"Gabriel",
"Luca",
"Ollie",
"Ben",
"Jude",
"Jamie",
"Evan",
"Owen",
"John",
"Tommy",
"Felix",
"Rory",
"Cameron",
"Aarav",
"Sam",
"Dexter",
"Nathaniel",
"Jason",
"Seth",
"Blake",
"Jasper",
"Leon",
"Stanley",
"Andrew",
"Bobby"]


def add_random_rooms(company, count=10):
    for i in range(count):
        company["rooms"].append({"name": "room number " + str(i+1), "capacity": random.randint(3, 20)})


def add_random_employees(company, count=10):
    for i in range(count):
        company["employees"].append({
            "name": names[i],
            "room_id": random.randint(0, len(company["rooms"])),
            "car_capacity": 0 if random.randint(0, 5) > 1 else random.randint(1, 4),
            "home_location": [31.774639 + random.random() / 3, 34.386373 + random.random() / 3],
            "shift_dependencies": set([random.randint(0, count) for _ in range(random.randint(0, 5))]),
            "capsule_dependencies": set([random.randint(0, count) for _ in range(random.randint(0, 5))]),
            "shift_availability": set([0,1] if random.randint(0, 5) < 2 else [random.randint(0, 1)])
        })

if __name__ == '__main__':
    add_random_rooms(companies["aa"])
    add_random_employees(companies["aa"])
    print(companies["aa"])

    employees = []
    employees_json = companies["aa"]["employees"]
    for i, employee in enumerate(employees_json):
        employees.append(Employee(
            identifier=i,
            room_id=employee["room_id"],
            home_location=employee["home_location"],
            car_capacity=employee["car_capacity"],
            shift_dependencies=employee["shift_dependencies"],
            capsule_dependencies=employee["capsule_dependencies"],
            shift_availability=employee["shift_availability"]))

    workspaces = []
    workspaces_json = companies["aa"]["rooms"]
    for i, room in enumerate(workspaces_json):
        workspaces.append(Workspace(
            identifier=i,
            capacity=room["capacity"]
           ))

    print(employees)
    print(workspaces)
    print(capsulize(10, 0.1, employees, workspaces))