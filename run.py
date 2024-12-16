from app import create_app

# Create the app instance using the create_app function
app = create_app()


def start_app():
    """
    Entry point for starting the app with a WSGI-compatible server.
    """
    app.run(debug=True)  # You can also set host='0.0.0.0' for external access


if __name__ == "__main__":
    start_app()
