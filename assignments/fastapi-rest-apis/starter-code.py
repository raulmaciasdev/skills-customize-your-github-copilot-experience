"""
FastAPI REST API Starter Code
Build a simple Note Management API

This starter provides the basic structure you need to get started.
Complete the tasks to build a fully functional API.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

# Initialize FastAPI app
app = FastAPI(
    title="Note Management API",
    description="A simple API for managing notes",
    version="1.0.0"
)

# Define Pydantic models for request/response validation
class Note(BaseModel):
    """Note model with id, title, content, and status"""
    id: int
    title: str
    content: str
    status: str = "active"  # Default status is "active"


class NoteCreate(BaseModel):
    """Model for creating a new note (without id)"""
    title: str
    content: str
    status: str = "active"


# In-memory database (replace with real database in production)
notes_db: List[Note] = [
    Note(id=1, title="First Note", content="This is the first note", status="active"),
    Note(id=2, title="Second Note", content="This is the second note", status="completed"),
]


@app.get("/")
def read_root():
    """Welcome endpoint"""
    return {"message": "Welcome to the Note Management API"}


@app.get("/notes", response_model=List[Note])
def get_all_notes(status: Optional[str] = None):
    """
    Retrieve all notes, optionally filtered by status
    
    Query Parameters:
    - status: Optional filter by note status
    """
    # TODO: Implement filtering by status if provided
    return notes_db


@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    """Retrieve a single note by ID"""
    # TODO: Find and return the note with the given ID
    # Return 404 error if not found
    pass


@app.post("/notes", response_model=Note, status_code=201)
def create_note(note: NoteCreate):
    """Create a new note"""
    # TODO: Create a new note with the next available ID
    # Add it to notes_db and return the created note
    pass


@app.put("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note_update: NoteCreate):
    """Update an existing note"""
    # TODO: Find the note with the given ID, update it, and return the updated note
    # Return 404 error if not found
    pass


@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    """Delete a note by ID"""
    # TODO: Find and delete the note with the given ID
    # Return 404 error if not found
    # Return a success message
    pass


if __name__ == "__main__":
    # To run this API:
    # pip install fastapi uvicorn
    # uvicorn starter-code:app --reload
    
    # Then visit http://localhost:8000/docs to see the interactive API documentation
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
