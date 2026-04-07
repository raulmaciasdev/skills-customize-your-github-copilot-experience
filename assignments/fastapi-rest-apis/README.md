# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build modern, production-ready REST APIs using the FastAPI framework. You'll create endpoints to handle HTTP requests, work with request/response models, and implement proper error handling and validation.

## 📝 Tasks

### 🛠️ Create a Basic Note Management API

#### Description

Build a simple REST API for managing notes (create, read, update, delete). Your API should accept JSON requests, validate input data, and return appropriate HTTP responses with error handling.

#### Requirements

Completed program should:

- Define note data models using Pydantic for validation
- Implement GET endpoint to retrieve all notes
- Implement POST endpoint to create a new note with validation
- Implement PUT endpoint to update an existing note
- Implement DELETE endpoint to remove a note
- Return appropriate HTTP status codes (200, 201, 404, 400)
- Include error messages for invalid requests
- Use path parameters and request bodies correctly

### 🛠️ Add Advanced API Features

#### Description

Enhance your API with filtering, error handling, and basic documentation. Implement query parameters for filtering notes and automatic API documentation generation.

#### Requirements

Completed program should:

- Add query parameters to filter notes (e.g., by status or search term)
- Implement custom error handling with descriptive messages
- Add detailed docstrings to endpoints for auto-generated documentation
- Use HTTP exception handlers for invalid data
- Test endpoints using tests or a tool like curl/Postman
- Ensure all endpoints follow REST conventions
