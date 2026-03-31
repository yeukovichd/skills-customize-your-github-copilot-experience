from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Homework Tracker API")


class Assignment(BaseModel):
    id: int
    subject: str
    title: str
    completed: bool = False


assignments = [
    {"id": 1, "subject": "Math", "title": "Algebra Practice", "completed": False},
    {"id": 2, "subject": "Science", "title": "Lab Report", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the Homework Tracker API!"}


@app.get("/assignments")
def get_assignments():
    # TODO: Return the full list of assignments.
    return {"assignments": assignments}


@app.get("/assignments/{assignment_id}")
def get_assignment(assignment_id: int):
    # TODO: Find the matching assignment by ID.
    # If no assignment is found, raise HTTPException(status_code=404, detail="Assignment not found")
    for assignment in assignments:
        if assignment["id"] == assignment_id:
            return assignment
    raise HTTPException(status_code=404, detail="Assignment not found")


@app.post("/assignments")
def create_assignment(assignment: Assignment):
    # TODO: Add the new assignment to the list and return it.
    assignments.append(assignment.model_dump())
    return {"created": assignment}


# Run with:
# uvicorn starter-code:app --reload
