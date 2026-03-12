# ============================== FASTAPI + MYSQL CRUD ==============================

from fastapi import FastAPI
from database import conn, cursor       # Import database connection and cursor from database.py
from pydantic import BaseModel          # Import BaseModel for request body validation
from fastapi import status              # Import status module to return HTTP status codes

app = FastAPI()                         # FastAPI application instance

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