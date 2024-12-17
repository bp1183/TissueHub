from datetime import datetime
import pytest
from app import create_app
from app.models import db, Collection, Sample


@pytest.fixture
def app():
    """Create a Flask app with a test configuration."""
    app = create_app(testing=True)
    with app.app_context():
        db.create_all()
    yield app
    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    """Create a test client."""
    return app.test_client()


@pytest.fixture
def init_db(app):
    """Initialize the database and create all tables."""
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()


def test_index(client, init_db, app):
    """Test the home page (index route) to see if collections are listed."""
    collection = Collection(title='Test Collection', disease_term='Test Disease')
    with app.app_context():
        db.session.add(collection)
        db.session.commit()

    # Test if the collection shows up in the index route
    response = client.get('/')
    assert response.status_code == 200
    assert b'Test Collection' in response.data


def test_new_collection(client):
    """Test creating a new collection."""
    response = client.get('/collections/new')
    assert response.status_code == 200
    assert b'Add Collection' in response.data

    response = client.post('/collections/new', data={
        'title': 'Test Collection',
        'disease_term': 'Test Disease'
    })
    assert response.status_code == 302  # Should redirect
    assert Collection.query.count() == 1  # Ensure that one collection is added


def test_collection_details(client):
    """Test viewing a collection's details."""
    collection = Collection(title="Test Collection", disease_term="Test Disease")
    db.session.add(collection)
    db.session.commit()

    response = client.get(f'/collections/{collection.id}')
    assert response.status_code == 200
    assert b'Test Collection' in response.data


def test_new_sample(client):
    """Test adding a new sample."""
    collection = Collection(title="Test Collection", disease_term="Test Disease")
    db.session.add(collection)
    db.session.commit()

    response = client.get(f'/collections/{collection.id}/samples/new')
    assert response.status_code == 200
    assert b'Add Sample' in response.data

    response = client.post(f'/collections/{collection.id}/samples/new', data={
        'collection_id': collection.id,
        'material_type': 'Test Material',
        'donor_count': 10,
        'last_updated': datetime.utcnow().strftime("%Y-%m-%d")
    })
    assert response.status_code == 302
    assert Sample.query.count() == 1
