import pytest
from app import create_app
from app.models import db, Collection


@pytest.fixture
def app():
    app = create_app(testing=True)
    yield app


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
