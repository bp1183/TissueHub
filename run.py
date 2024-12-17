from app import create_app

app = create_app()


def start_app():
    """
    Entry point for starting the app with a WSGI-compatible server.
    """
    app.run(debug=True)


if __name__ == "__main__":
    start_app()
