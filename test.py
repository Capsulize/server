import requests
import random

url = 'http://192.168.43.18:5555'
company = {
    "rooms": [],
    "shifts": ["08:00 - 15:00", "16:00 - 23:00", "2", "3", "4"],
    "employees": []
}
company_name = "Amazon"

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
        company["rooms"].append({"name": "room number " + str(i + 1), "capacity": random.randint(3, 20)})


def add_room(company, room_id, capacity):
    company["rooms"].append({"name": "room number " + str(room_id), "capacity": capacity})


def generate_random_employee(company):
    return {"name": names[random.randint(0, len(names))],
            "room_id": random.randint(0, len(company["rooms"])),
            "car_capacity": 0 if random.randint(0, 5) > 1 else random.randint(1, 4),
            "home_location": [31.774639 + random.random() / 3, 34.386373 + random.random() / 3],
            "shift_dependencies": list(
                set([random.randint(0, len(company["employees"])) for _ in range(random.randint(0, 5))])),
            "capsule_dependencies": list(
                set([random.randint(0, len(company["employees"])) for _ in range(random.randint(0, 5))])),
            "shift_availability": list(set([0, 1] if random.randint(0, 5) < 2 else [random.randint(0, 1)]))
            }


def generate_employee(name, room_id, shift_dependencies, capsule_dependencies, shift_availability):
    return {"name": name,
            "room_id": room_id,
            "car_capacity": 0 if random.randint(0, 5) > 1 else random.randint(1, 4),
            "home_location": [31.774639 + random.random() / 3, 34.386373 + random.random() / 3],
            "shift_dependencies": shift_dependencies,
            "capsule_dependencies": capsule_dependencies,
            "shift_availability": shift_availability
            }


# add_random_rooms(company)
# x = requests.post(url + "/" + company_name, json=company)

# for _ in range(1):
#     employee = generate_random_employee(company)
#     x = requests.post(url + "/" + company_name + "/" + "employee", json=employee)

# #
# # requests.get(url + "/" + company_name)

add_room(company, 1, 5)
add_room(company, 2, 5)
add_room(company, 3, 5)

employee = [
    generate_employee(13, 0, [], [], [3]), generate_employee(1, 1, [], [], [1, 2]),
    generate_employee(2, 1, [3, 4], [4], [1, 2]), generate_employee(3, 1, [], [], [1, 2]),
    generate_employee(4, 1, [5], [5], [1]), generate_employee(5, 1, [3], [], [1]),
    generate_employee(6, 2, [7], [7], [2]), generate_employee(7, 2, [8], [], [2]),
    generate_employee(8, 2, [6], [6], [1, 2]), generate_employee(9, 0, [10, 11, 12], [10, 11, 12], [1, 2]),
    generate_employee(10, 0, [9, 11, 12], [9, 11, 12], [1, 2]),
    generate_employee(11, 0, [9, 10, 12], [9, 10, 12], [1, 2]),
    generate_employee(12, 0, [9, 10, 11], [9, 10, 11], [1, 2]), generate_employee(13, 1, [14, 15], [], [3, 4]),
    generate_employee(14, 1, [15], [15], [3, 4]), generate_employee(15, 0, [16], [16], [3, 4]),
    generate_employee(16, 0, [13], [], [3, 4])
]

x = requests.post(url + "/" + company_name, json=company)

for i in range(len(employee)):
    x = requests.post(url + "/" + company_name + "/" + "employee", json=employee[i])

requests.post(url + "/" + company_name + "/" + "capsulize")
