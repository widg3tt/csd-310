# Kyle Jones
# 4/8/2022
# Module 5.3

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ngnuu.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech

print("\n")

print("-- DISPLAYING STUDENTS FROM find() QUERY --")
for record in db.students.find({}):
    print(record)

print("\n")

print("-- DISPLAYING STUDENT FROM find_one() QUERY --")
doc = db.students.find_one({"student_id": 1009})
print(doc)
