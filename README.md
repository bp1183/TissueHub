# TissueHub: Tissue Sample Directory
A Flask-based web application for managing collections of tissue samples and their associated metadata.

## Features
### 1. Display Collections (Home Page)
- **Route**: `/`
- Fetches all collections stored in the database.
- Displays a list of collections with their respective titles and associated disease terms.

### 2. View Collection Details
- **Route**: `/collection/<id>`
- Displays detailed information about a specific collection, including its samples (donor count, material type, last updated).

### 3. Add a Sample to a Collection
- **Route**: `/collection/<id>/add-sample`
- Provides a form to input sample details including:
    - Donor count
    - Material type
    - Last updated date (defaults to the current date)
- Saves the new sample to the database.

### 4. Create a New Collection
- **Route**: `/collection/add`
- Allows users to create a new collection by providing the following details:
    - Title
    - Disease term
- Saves the new collection to the database.

## Getting Started
### Prerequisites
- Python 3.10+
- Poetry (used for managing dependencies)

## Installation
### 1. Clone this repository
```bash
git clone https://github.com/bp1183/TissueHub.git
cd TissueHub
```
### 2. Install Poetry
If you don't have poetry installed, you can install it by following the [official installation guide](https://python-poetry.org/docs/#installation).
### 3. Install dependencies using Poetry
```bash
poetry install
```
This will install all required dependencies as specified in the pyproject.toml.


### 4. Set up the database
First, initialize the Flask-Migrate migration environment:
```bash
poetry run flask db init
```
Next, generate the migration script for creating the initial database tables:
```bash
poetry run flask db migrate -m "Initial migration"
```
Apply the migration to create the tables in the database:
```bash
poetry run flask db upgrade
```
Finally, populate the database with the seed data
```bash
poetry run flask init-db
```
### 5. Run the application
```bash
poetry run start
```

### 6. Access the app
Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Tests
Test can be run using `pytest`:
```bash
poetry run pytest
```