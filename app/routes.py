from datetime import datetime
from flask import render_template, request, redirect, url_for, flash
from app.models import db, Collection, Sample


def index():
    """Home page: Display all collections."""
    collections = Collection.query.all()
    return render_template("index.html", collections=collections)


def collection_details(collection_id):
    """View details of a specific collection and its samples."""
    collection = Collection.query.get_or_404(collection_id)
    return render_template("collection_details.html", collection=collection)


def new_collection():
    """Add a new collection."""
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
            return redirect(url_for("index"))

    return render_template("new_collection.html")


def new_sample(collection_id):
    """Add a new sample to an existing collection."""
    collection = Collection.query.get_or_404(collection_id)

    if request.method == "POST":
        material_type = request.form.get("material_type")
        donor_count = request.form.get("donor_count")
        last_updated_str = request.form.get("last_updated")  # Get the user-provided last_updated

        # Check if both material_type and donor_count are provided
        if not material_type or not donor_count or not last_updated_str:
            flash("Material type, donor count, and last updated are required!", "error")
        else:
            try:
                # Try to convert last_updated to a datetime object
                last_updated = datetime.strptime(last_updated_str, "%Y-%m-%d")
                donor_count = int(donor_count)
            except ValueError:
                flash("Invalid date format or donor count. Please use the correct format!", "error")
                return render_template("new_sample.html", collection=collection)

            # Create and save the new sample
            new_sample = Sample(
                collection_id=collection.id,
                material_type=material_type,
                donor_count=donor_count,
                last_updated=last_updated  # Set the user-provided last_updated datetime
            )
            db.session.add(new_sample)
            db.session.commit()
            flash("Sample added successfully!", "success")
            return redirect(url_for("collection_details", collection_id=collection.id))

    return render_template("new_sample.html", collection=collection)
