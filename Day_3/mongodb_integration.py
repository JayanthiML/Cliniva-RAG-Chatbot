from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['school']
collection = db['students']

for student in collection.find():
    print(student)