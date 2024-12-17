from datetime import datetime
import pytest
from app import create_app
from app.models import db, Collection, Sample


@pytest.fixture
def app():
    """Create a Flask app with a test configuration."""
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()  # Create tables in the test database
    yield app
    with app.app_context():
        db.drop_all()  # Clean up after the test


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


@pytest.fixture
def init_db(app):
    """Initialize the database and create all tables."""
    with app.app_context():
        db.create_all()  # Create the tables
        yield db
        db.session.remove()
        db.drop_all()


def test_index(client, init_db, app):
    """Test the home page (index route) to see if collections are listed."""
    # Create a sample collection for testing
    collection = Collection(title='Test Collection', disease_term='Test Disease')

    # Use the app context here to add data to the database
    with app.app_context():
        db.session.add(collection)
        db.session.commit()

    # Now test if the collection shows up in the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Collection' in response.data


# Test creating a new collection
def test_new_collection(client):
    response = client.get('/collections/new')
    assert response.status_code == 200
    assert b'Add Collection' in response.data

    # Create a collection
    response = client.post('/collections/new', data={
        'title': 'Test Collection',
        'disease_term': 'Test Disease'
    })
    assert response.status_code == 302  # Should redirect
    assert Collection.query.count() == 1  # Ensure that one collection is added


# Test viewing a collection's details
def test_collection_details(client):
    collection = Collection(title="Test Collection", disease_term="Test Disease")
    db.session.add(collection)
    db.session.commit()

    response = client.get(f'/collections/{collection.id}')
    assert response.status_code == 200
    assert b'Test Collection' in response.data


# Test adding a new sample
def test_new_sample(client):
    collection = Collection(title="Test Collection", disease_term="Test Disease")
    db.session.add(collection)
    db.session.commit()

    response = client.get(f'/collections/{collection.id}/samples/new')
    assert response.status_code == 200
    assert b'Add Sample' in response.data

    # Create a new sample
    response = client.post(f'/collections/{collection.id}/samples/new', data={
        'collection_id': collection.id,
        'material_type': 'Test Material',
        'donor_count': 10,
        'last_updated': datetime.utcnow().strftime("%Y-%m-%d")
    })
    assert response.status_code == 302  # Should redirect after POST
    assert Sample.query.count() == 1  # Ensure the sample is added
