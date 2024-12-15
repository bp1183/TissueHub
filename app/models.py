from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Collection(db.Model):
    """Model for tissue sample collections."""
    __tablename__ = "collections"
    id = db.Column(db.Integer, primary_key=True)
    disease_term = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)

    # Relationship to access samples in a collection
    samples = db.relationship("Sample", back_populates="collection", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Collection id={self.id} title={self.title} disease_term={self.disease_term}>"


class Sample(db.Model):
    """Model for individual samples within a collection."""
    __tablename__ = "samples"

    id = db.Column(db.Integer, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"), nullable=False)
    donor_count = db.Column(db.Integer, nullable=False)
    material_type = db.Column(db.String(100), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship to link sample back to collection
    collection = db.relationship("Collection", back_populates="samples")

    def __repr__(self):
        return f"<Sample id={self.id} collection_id={self.collection_id} donor_count={self.donor_count} material_type={self.material_type}>"

