# ============================== FASTAPI + MYSQL CRUD ==============================

from fastapi import FastAPI

# Import database connection and cursor from database.py
# conn   -> connection object used to commit transactions
# cursor -> used to execute SQL queries
from database import conn, cursor

# Import BaseModel for request body validation
from pydantic import BaseModel

# Import status module to return HTTP status codes
from fastapi import status

# Create FastAPI application instance
app = FastAPI()

# ---------------------------- STUDENT MODEL ----------------------------
# This Pydantic model is used to:
# 1. Validate incoming JSON request data
# 2. Ensure correct datatype
# 3. Automatically convert JSON to Python object

class Student(BaseModel):
    id: int
    name: str
    age: int


# ---------------------------- POST ENDPOINT ----------------------------
# Endpoint to INSERT student data into MySQL database

@app.post('/students')
def add_students(student: Student):

    # SQL query to insert student record
    query = 'INSERT INTO students (id, name, age) VALUES (%s, %s, %s)'

    # Values are taken from the student object received from request body
    values = (student.id, student.name, student.age)

    # Execute INSERT query
    cursor.execute(query, values)

    # to permanently save changes
    conn.commit()   

    # success message
    return {'message': 'Student added to MySQL'}

# ---------------------------- GET BY ID ----------------------------
# fetches a student record using ID
# student_id is received as PATH PARAMETER from URL

@app.get('/students/{student_id}')
def get_student(student_id: int):

    # SQL query to fetch student record
    query = 'SELECT * FROM students WHERE id = %s'

    cursor.execute(query, (student_id,))

    # Fetch one record from result
    data = cursor.fetchone()

    # If record found
    if data:
        return {
            'id': data[0],
            'name': data[1],
            'age': data[2]
        }

    # If record not found
    return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}

# ---------------------------- PUT (UPDATE) ----------------------------
# Updates existing student record using student_id from URL

@app.put('/students/{student_id}')
def update_student(student_id:int, student: Student):

    # SQL query to update name and age
    query = 'UPDATE students SET name=%s, age=%s WHERE id=%s'

    # Values taken from request body + path parameter
    values = (student.name, student.age, student_id)

    cursor.execute(query, values)

    conn.commit()

    # returns number of rows affected
    if cursor.rowcount > 0:
        return {"message": "Student updated successfully", "status": status.HTTP_200_OK}

    return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}

# ---------------------------- DELETE ----------------------------
# Deletes student record using ID

@app.delete('/students/{student_id}')
def delete_student(student_id: int):

    query = 'DELETE FROM students WHERE id=%s'

    cursor.execute(query, (student_id,))

    conn.commit()

    if cursor.rowcount > 0:
        return {"message": "Student deleted successfully", "status": status.HTTP_200_OK}

    return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}


# # ============================== FASTAPI + MONGODB CRUD ==============================

# # Import FastAPI framework to create API endpoints
# from fastapi import FastAPI

# # Import MongoDB collection from database.py
# # student_collection -> represents MongoDB collection (like table in SQL)
# from database import student_collection

# # Import BaseModel for request body validation
# from pydantic import BaseModel

# # Import status module to return HTTP status codes
# from fastapi import status

# # Create FastAPI application instance
# app = FastAPI()


# # ---------------------------- STUDENT MODEL ----------------------------
# # This Pydantic model is used to:
# # 1. Validate incoming JSON request data
# # 2. Ensure correct datatype
# # 3. Automatically convert JSON to Python object

# class Student(BaseModel):
#     id: int
#     name: str
#     age: int


# # ---------------------------- POST ENDPOINT ----------------------------

# @app.post('/students')
# def add_students(student: Student):

#     # Convert Pydantic object -> Python dictionary
#     # MongoDB accepts dictionary format only
#     student_dict = student.dict()

#     # Insert into DB
#     student_collection.insert_one(student_dict)

#     return {'message': 'Student added to MongoDB'}

# # ---------------------------- GET BY ID ----------------------------

# @app.get('/students/{student_id}')
# def get_student(student_id: int):

#     # find_one() fetches single document matching condition
#     # {'_id':0} excludes MongoDB default ObjectId field
#     data = student_collection.find_one({"id": student_id}, {'_id':0})

#     if data:
#         return data

#     return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}

# # ---------------------------- PUT (UPDATE) ----------------------------

# @app.put('/students/{student_id}')
# def update_student(student_id: int, student: Student):

#     update_data = student.dict()

#     # update_one() updates matching document
#     # $set updates only specified fields
#     result = student_collection.update_one(
#         {"id": student_id},
#         {"$set": update_data}
#     )

#     if result.matched_count > 0:
#         return {"message": "Student updated successfully", "status": status.HTTP_200_OK}

#     return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}

# # ---------------------------- DELETE ----------------------------

# @app.delete('/students/{student_id}')
# def delete_student(student_id: int):

#     result = student_collection.delete_one({"id": student_id})

#     if result.deleted_count > 0:
#         return {"message": "Student deleted successfully", "status": status.HTTP_200_OK}

#     return {"message": "Student not found", "status": status.HTTP_404_NOT_FOUND}


# ==========================================================================================

# ### Basic API Creation

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# ## 1. Create sample in-memory list (students)
# students = list()                   # sample in-memory list

# ## 2. Create GET endpoint
# @app.get('/students')
# def get_students():
#     return students

# ## 3. Create POST endpoint

# # create student model
# class Student(BaseModel):
#     id: int
#     name: str
#     age: int


# # POST endpoint
# @app.post("/students")
# def add_student(student: Student):
#     students.append(student)
#     return {"message": "Student added successfully"}

# ----------------------------------------------------------------------------------------

# # BASIC
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/')
# async def hello():
#     return 'welcome to fastapi'
# # This returns the 'welcome to fastapi' on clicking on the URL

# ------------------------------------------------------------------------------------

# # PATH PARAMETER
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/welcome/{name}')
# async def hello(name):
#     return 'welcome ' +name+ ", to fastapi"
# # This returns the 'welcome to fastapi' on clicking on the URL

# --------------------------------------------------------------------------------------

# # PATH PARAMETER - DATA TYPE
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/books/{book_id}/{book_name}')
# async def books(book_id : int, book_name):
#     return 'Book ID: ' +str(book_id)+ ", Book Name: " +book_name
# # This returns the 'welcome to fastapi' on clicking on the URL 

# -----------------------------------------------------------------------------------------

# # PATH PARAMETER - DEFAULT
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/books/default')
# async def books():
#     return 'Python Programming'

# @app.get('/book/{book_name}')
# async def hello(book_name):
#     return book_name
# # This returns the 'welcome to fastapi' on clicking on the URL 

# ----------------------------------------------------------------------------------------

# # PATH PARAMETER
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/')
# async def welcome():
#     return "Welcome to Practice of FastAPI"

# @app.get('/books/{book_id}')
# async def book(book_id):
#     books_data = {
#         '1001' : 'Python',
#         '1002' : 'Java',
#         '1003' : 'C++',
#         '1004' : 'HTML',
#         '1005' : 'JAVASCRIPT'
#         }
#     return {f'Book ID : {book_id} and Book Name : {books_data[book_id]}'}
# # This returns the 'welcome to fastapi' on clicking on the URL 

# --------------------------------------------------------------------------------------

# # QUERY PARAMETER
# from fastapi import FastAPI

# app = FastAPI()

# @app.get('/')
# async def welcome():
#     return "Welcome to Practice of FastAPI"

# @app.get('/book/')          # no need to mention parameter in URL
#                             # URL will be like http://127.0.0.1:8000/book/?limit=1
# async def book(limit: int):
#     books_data = [
#     {'1001': 'Python'},
#     {'1002': 'Java'},
#     {'1003': 'C++'},
#     {'1004': 'HTML'},
#     {'1005': 'JAVASCRIPT'}
# ]
#     return {f'Book Data is {books_data[:limit]}'}
# # This returns the 'welcome to fastapi' on clicking on the URL 