import pytest
from app import create_app
from app.models import db, Collection, Sample
from datetime import datetime


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
def sample_data(app):
    """Fixture to add sample data."""
    collection = Collection(title="Test Collection", disease_term="Test Disease")
    db.session.add(collection)
    db.session.commit()

    sample = Sample(
        collection_id=collection.id,
        material_type="Test Material",
        donor_count=5,
        last_updated=datetime.utcnow().date()
    )
    db.session.add(sample)
    db.session.commit()
    return sample


def test_collection_creation(sample_data):
    """Test the collection model."""
    collection = sample_data.collection
    assert collection.title == "Test Collection"
    assert collection.disease_term == "Test Disease"


def test_sample_creation(sample_data):
    """Test the Sample model,"""
    sample = sample_data
    assert sample.material_type == "Test Material"
    assert sample.donor_count == 5
    assert sample.last_updated is not None


def test_collection_samples_query(sample_data):
    """Test querying for a collection's samples."""
    collection = sample_data.collection
    samples = collection.samples  # Access related samples via SQLAlchemy relationship
    assert len(samples) == 1  # Should return 1 sample
    assert samples[0].material_type == "Test Material"
