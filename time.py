from dbio import load
from dbio import save
from dbio import export

from routine import print_record
from routine import find_record
from routine import add_record
from routine import delete_record

data = []

with open("dataset.txt","r") as file:
    for line in file:
        data.append(line.replace("\n",""))

path = "temp.txt"

temp = open(path, "tw")
temp.close

records = []

import random
import time

random.seed()

for i in range(0, 10000):

    records.append("{},{},{},{}".format(str(i), data[random.randint(0, len(data) - 1)], data[random.randint(0, len(data) - 1)], data[random.randint(0, len(data) - 1)]))

print("Dataset loaded")
print("Random records created")
print("Start measuring time")
print("")

start = time.time()
db = load(path)
end = time.time()
print("Loading empty db")
print(end - start)


start = time.time()
for record in records:
    add_record(db, record)
end = time.time()
print("Add 10000 records")
print(end - start)

start = time.time()
save(db, path)
end = time.time()
print("Save db with 10000 records")
print(end - start)

start = time.time()
db = load(path)
end = time.time()
print("Load db with 10000 records")
print(end - start)

start = time.time()
for i in range(0, 10000):
    find_record(db, records[random.randint(0, len(records) - 1)])
end = time.time()
print("Find 10000 times")
print(end - start)

start = time.time()
for record in records:
    delete_record(db, db[-1])
end = time.time()
print("Delete 10000 records")
print(end - start)

start = time.time()
save(db, path)
end = time.time()
print("Save db with 10000 deleted records")
print(end - start)
