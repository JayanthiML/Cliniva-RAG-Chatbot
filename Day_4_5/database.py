# MYSQL CONNECTION CODE

import mysql.connector

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root123',
    database = 'student_db'                 # we are using an existing db
)

cursor = conn.cursor()



# # MONGODB CONNECTION CODE

# from pymongo import MongoClient

# client = MongoClient("mongodb://localhost:27017")

# db = client["student_db"]

# student_collection = db["students"]