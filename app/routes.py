from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, Collection, Sample

main = Blueprint("main", __name__)


# Home page: Display all collections
@main.route("/")
def index():
    collections = Collection.query.all()
    return render_template("index.html", collections=collections)


# View details of a specific collection and its samples
@main.route("/collections/<int:collection_id>")
def collection_details(collection_id):
    collection = Collection.query.get_or_404(collection_id)
    return render_template("collection_details.html", collection=collection)


# Add a new collection
@main.route("collections/new", methods=["GET", "POST"])
def add_new_collection():
    if request.method == "POST":
        title = request.form.get("title")
        disease_term = request.form.get("title")
        if not title or not disease_term:
            flash("Both title and disease term are required!", "error")
        else:
            # Create a new collection and save it to the database
            new_collection = Collection(title=title, disease_term=disease_term)
            db.session.add(new_collection)
            db.session.commit()
            flash("Collection added successfully!", "success")
            return redirect(url_for("main.index"))

    return render_template("new_collection.html")


# Add a new sample to an existing collection
@main.route("/collections/<int:collection_id>/samples/new", methods=["GET", "POST"])
def new_sample(collection_id):
    collection = Collection.query.get_or_404(collection_id)
    if request.method == "POST":
        material_type = request.form.get("material_type")
        donor_count = request.form.get("donor_count")
        if not material_type or not donor_count:
            flash("Both material type and donor count are required!", "error")
        else:
            try:
                donor_count = int(donor_count)
            except ValueError:
                flash("Donor count must be a number!", "error")
                return render_template("new_sample.html", collection=collection)

            # Create a new sample and associate it with the collection
            new_sample = Sample(collection_id=collection.id, material_type=material_type, donor_count=donor_count)
            db.session.add(new_sample)
            db.session.commit()
            flash("Sample added sucessfully!", "success")
            return redirect(url_for("main.collection_details", collection_id=collection.id))

    return render_template("new_sample.html", collection=collection)
