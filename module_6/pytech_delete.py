# Kyle Jones
# 4/14/2022
# Module 6.3
# https://github.com/widg3tt/csd-310

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ngnuu.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
students = db["students"]

jake = {
    "student_id": 1010,
    "first_name": "Jake",
    "last_name": "Miller"
}

print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for record in students.find():
  print(record)

jake_record = students.insert_one(jake).inserted_id
str_jake = str(jake_record)

print("\n")
print("-- INSERT STATEMENTS --")
print("Inserted student record into the students collection with document_id: " + str_jake)

print("\n")
print("-- DISPLAYING STUDENT TEST DOC --")
doc = db.students.find_one({"student_id": 1010})
print(doc)

myquery = { "student_id": 1010 }

students.delete_one(myquery)

print("\n")
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for record in students.find():
  print(record)