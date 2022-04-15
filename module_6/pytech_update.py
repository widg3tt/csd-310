# Kyle Jones
# 4/14/2022
# Module 6.2
# https://github.com/widg3tt/csd-310

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ngnuu.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
students = db["students"]

print("\n")
print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for record in students.find():
  print(record)

myquery = { "student_id": 1007 }
newvalues = { "$set": { "last_name": "Johnson" } }

students.update_one(myquery, newvalues)
print("\n")
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
doc = db.students.find_one({"student_id": 1007})
print(doc)