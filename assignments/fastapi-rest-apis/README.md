# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Use the FastAPI framework to build a small REST API that serves JSON data and accepts new records from users. By the end of this assignment, you will understand how API routes, request methods, and data validation work together.

## 📝 Tasks

### 🛠️	Create Basic API Routes

#### Description
Set up a FastAPI app in `starter-code.py` and create a few `GET` endpoints for a simple homework tracker API.

#### Requirements
Completed program should:

- Create a FastAPI app object named `app`
- Add a `GET /` route that returns a welcome message in JSON format
- Add a `GET /assignments` route that returns a list of sample assignments


### 🛠️	Add Input Validation and Lookup

#### Description
Expand your API so users can view one assignment by ID and submit a new assignment using a `POST` request.

#### Requirements
Completed program should:

- Add a `GET /assignments/{assignment_id}` route that returns one assignment or an error if it does not exist
- Create a Pydantic model to validate data sent to a `POST /assignments` route
- Test your finished API using FastAPI's built-in `/docs` page
