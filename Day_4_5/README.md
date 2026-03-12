# FastAPI CRUD API

## Project Overview

This project demonstrates building a **REST API using FastAPI** with **database integration and CRUD operations**.

# Project Structure

```
project_folder
│
├── workings.py      # FastAPI learning experiments
├── main.py          # Final CRUD API implementation
├── database.py      # Database connection configuration
└── README.md
```

---

# 1. FastAPI Learning Experiments (workings.py)

Before building the final project, multiple FastAPI concepts were explored in **workings.py**.

### 1. Basic FastAPI Application

A basic FastAPI app was created to understand how APIs work.

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello():
    return "welcome to fastapi"
```

This helped understand:

* Creating a FastAPI application
* Running an API server
* Returning responses

---

### 2. Path Parameters

Path parameters were explored to understand how values can be passed through URLs.

Example:

```python
@app.get('/welcome/{name}')
async def hello(name):
    return "welcome " + name
```

Example request:

```
/welcome/Jayanthi
```

Response:

```
welcome Jayanthi
```

This demonstrated how FastAPI extracts values directly from the URL.

---

### 3. Path Parameters with Data Types

FastAPI allows specifying **data types for path parameters**.

Example:

```python
@app.get('/books/{book_id}/{book_name}')
async def books(book_id: int, book_name):
    return "Book ID: " + str(book_id) + ", Book Name: " + book_name
```

This ensures the correct datatype is received.

---

### 4. Query Parameters

Query parameters were tested to pass values in the URL query string.

Example:

```python
@app.get('/book/')
async def book(limit: int):
    books_data = [
        {'1001': 'Python'},
        {'1002': 'Java'}
    ]
    return books_data[:limit]
```

Example request:

```
/book/?limit=1
```

This returns only a limited number of results.

---

### 5. In-Memory Data Storage

Before integrating databases, a simple **Python list was used to simulate a database**.

Example:

```python
students = list()
```

Two endpoints were created:

GET endpoint

```python
@app.get('/students')
def get_students():
    return students
```

POST endpoint

```python
@app.post('/students')
def add_student(student: Student):
    students.append(student)
```

This helped understand:

* Request body handling
* JSON data processing
* API behavior without a database

---

### 6. Pydantic Data Model

A **Pydantic model** was created for validating incoming request data.

Example:

```python
class Student(BaseModel):
    id: int
    name: str
    age: int
```

Benefits:

* Ensures correct data types
* Automatically converts JSON to Python objects
* Provides request validation

---

# 2. Final API Implementation (main.py)

After experimenting with FastAPI features, the final API was implemented in **main.py**.

The API performs **CRUD operations on student records stored in a database**.

The FastAPI application is initialized as:

```python
app = FastAPI()
```

The database connection is imported from **database.py**. 

---

# Student Model

The `Student` model is defined using Pydantic.

```python
class Student(BaseModel):
    id: int
    name: str
    age: int
```

This model is used to validate request data for API operations.

---

# CRUD Endpoints

### POST – Add Student

Endpoint:

```
POST /students
```

Function:

```
add_students()
```

Purpose:

Insert a new student record into the database.

Process:

1. Receive request body
2. Validate using Student model
3. Execute SQL INSERT query
4. Commit changes to database

---

### GET – Retrieve Student

Endpoint:

```
GET /students/{student_id}
```

Function:

```
get_student()
```

Purpose:

Fetch a student record using the student ID.

If the student exists, the API returns student details.

If not, a **404 status message** is returned.

---

### PUT – Update Student

Endpoint:

```
PUT /students/{student_id}
```

Function:

```
update_student()
```

Purpose:

Update student information such as name and age.

The API checks whether the record exists before returning a success response.

---

### DELETE – Remove Student

Endpoint:

```
DELETE /students/{student_id}
```

Function:

```
delete_student()
```

Purpose:

Delete a student record from the database.

The API confirms whether a record was deleted using the database response.

---

# 3. Database Configuration (database.py)

The database connection is defined in **database.py**.

MySQL was used as the primary database.

The `conn` object manages the database connection and commits transactions.

The `cursor` object executes SQL queries. 

---

# MongoDB Experimentation

In addition to MySQL, MongoDB integration was also explored.

MongoDB operations included:

* `insert_one()`
* `find_one()`
* `update_one()`
* `delete_one()`

This was implemented to understand the difference between:

Relational databases (MySQL)
Non-relational databases (MongoDB)

---

# Running the Application

Start the FastAPI server using Uvicorn.

```
uvicorn main:app --reload
```

Server URL:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically generates API documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

# API Testing

All endpoints were tested using **Postman** and **Swagger UI**.

Test scenarios included:

* Creating student records
* Fetching student data
* Updating records
* Deleting records
* Handling invalid requests

---

# Conclusion

This project demonstrates:

* Learning FastAPI fundamentals
* Building REST APIs
* Request validation using Pydantic
* CRUD operations
* MySQL database integration
* MongoDB experimentation
* API testing using Postman
* Version control using Git