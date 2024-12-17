# Tissue Sample Directory
A Flask-based web application for managing collections of tissue samples and their associated metadata.

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

## Getting Started
### Prerequisites
- Python 3.10+
- Poetry
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

### 4. Set up the database
Initialise the migration environment
```bash
poetry run flask db init
```
Generate the migration scripts (also will create the necessary tables in the database)
```bash
poetry run flask db migrate -m "Initial migration"
```
Apply the migrations
```bash
poetry run flask db upgrade
```

### 5. Run the application
```bash
poetry run start
```

### 6. Access the app
Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)