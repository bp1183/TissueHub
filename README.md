# Tissue Sample Application
## Technology Stack
- Backend framework: Python with Flask or Django
    - Flask: Lightweight and perfect for quick prototyping
    - Django: Includes robust ORM and admin interface
- Frontend framework:
    - Use Flask/Django templates (Jinja2)
    - Optionally use React or Vue.js for a more dynamic UI
- Database: SQLite for simplicity (or PostgreSQL for future scalability).
- ORM: SQLAlchemy (if Flask) or Django’s built-in ORM.
- Styling: Use Bootstrap or Tailwind CSS for a clean UI.

## Architecture Design
Follow Model-View-Controller (MVC) or similar architecture.

### Entities and Models
Define database models for Collections and Samples.

1.  Collection Model
    - `id`: Integer, Primary Key
    - `disease_term`: String
    - `title`: String
2. Sample Model
    - `id`: Integer, Primary Key
    - `collection_id`: Foreign Key
    - `donor_count`: Integer
    - `material_type`: String
    - `last_updated`: DateTime

## Features

### 1. Display Collections (Home Page)
Route: `/`
- Fetch all collections from the database.
- Render a list with each collection’s title and disease_term.

### 2. View Collection Details
Route: `/collection/<id>`
- Fetch a single collection by id.
- Display associated samples (donor_count, material_type, last_updated).

### 3. Add a Sample to a Collection
Route: `/collection/<id>/add-sample`
- Form to accept sample details:
    - donor_count
    - material_type
    - last_updated (default: current date)
- Save to the Samples table.

### 4. Create a New Collection
Route: `/collection/add`
- Form to accept collection details:
    - title
    - disease_term
- Save to the Collections table.

## Development Workflow
1. Set Up Environment
    - Poetry for dependency management.

2. Define Models
    - Use SQLAlchemy/Django models to define Collections and Samples.

3. Create CRUD Operations
    - Use Flask/Django routes or views to handle database operations.

4. Build Templates
    - Use Jinja2 for templates (or React/Vue for dynamic rendering).
    - Use Bootstrap for responsiveness.

5. Write Documentation
    - Include a README with:
        - Installation instructions.
        - Steps to set up the database.
        - How to run the application.

## Implementation
### Backend
1. Database Initialization
    - Define models, and use migrations (Flask-Migrate or Django migrations).

2. CRUD Operations
    - Create endpoints for collections and samples.

### Frontend
1. Use Bootstrap for layout and forms.
2. Create templates for:
    - Home page.
    - Collection details.
    - Add forms for new collection and sample.

### Testing
- Write unit tests using `pytest` or Django’s testing framework.
- Test CRUD operations and ensure API correctness.

## Deployment
1.  Use a service like Heroku or Railway.app for hosting.
2. Add instructions for running the application locally and deploying it.

## Overview of Model-View-Controller (MVC) Architecture in Flask
### 1. Model
- Represents the data layer and the logic to interact with the database
- Encapsulates the database schema and handles the CRUD operations
- The `model.py` file defines the `Collection` and `Sample` models.

### 2. View
- Represents the presentation layer, which displays data to the user.
- Usually implemented as HTML templates rendered by Flask
- Example: `index.html`, `collection.html`, and `add_collection.html`.

### 3. Controller
- Represents the application logic and handles user interactions.
- Connects the model and the view, coordinating their interactions.
- The `routes.py` file contains the functions that process user requests and manage data.

## Installation Instructions
Poetry is used to manage packages and dependencies.

Use the command
```bash
poetry shell
```
to activate the vritual environment for the project.

