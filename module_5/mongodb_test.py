# Kyle Jones
# 4/7/2022
# Module 5.2

from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.ngnuu.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url, tls=True, tlsAllowInvalidCertificates=True)
db = client.pytech
collection = db.list_collection_names()
print(collection)