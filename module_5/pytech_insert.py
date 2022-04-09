# Kyle Jones
# 4/8/2022
# Module 5.3

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ngnuu.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
students = db["students"]

kyle = {
    "student_id": 1007,
    "first_name": "Kyle",
    "last_name": "Jones"
}

stephanie = {
    "student_id": 1008,
    "first_name": "Stephanie",
    "last_name": "Harris"
}

tiffany = {
    "student_id": 1009,
    "first_name": "Tiffany",
    "last_name": "Johnson"
}

kyle_record = students.insert_one(kyle).inserted_id
stephanie_record = students.insert_one(stephanie).inserted_id
tiffany_record = students.insert_one(tiffany).inserted_id

print("-- INSERT STATEMENTS --")

print(kyle_record)
print(stephanie_record)
print(tiffany_record)