from datetime import datetime
from app import create_app
from app.models import db, Collection, Sample


app = create_app()


def initialise_db():
    with app.app_context():
        collections = Collection.query.all()
        if not collections:
            collection_1 = Collection(title="Mothers Pregnancy Samples", disease_term="Cirrhosis of liver")
            collection_2 = Collection(title="Phase 2 multicentre study", disease_term="Malignant tumour of the breast")
            collection_3 = Collection(title="Lymphoblastoid cell lines", disease_term="Fit and well")
            collection_4 = Collection(title="Samples available include ME/CFS Cases", disease_term="Chronic fatigue syndrome")
            collection_5 = Collection(title="A randomised placebo-controlled trial", disease_term="Malignant tumour of breast")

            db.session.add(collection_1)
            db.session.add(collection_2)
            db.session.add(collection_3)
            db.session.add(collection_4)
            db.session.add(collection_5)
            db.session.commit()

            sample_1 = Sample(collection_id=4, material_type="Cerebrospinal fluid", donor_count=90210, last_updated=datetime(2019, 6, 3))
            sample_2 = Sample(collection_id=2, material_type="Cerebrospinal fluid", donor_count=512, last_updated=datetime(2019, 3, 8))
            sample_3 = Sample(collection_id=2, material_type="Core biopsy", donor_count=7777, last_updated=datetime(2019, 5, 4))

            db.session.add(sample_1)
            db.session.add(sample_2)
            db.session.add(sample_3)
            db.session.commit()

            print("Initial data added successfully.")
        else:
            print("Database already contains data.")


if __name__ == "__main__":
    initialise_db()
