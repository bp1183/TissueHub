from app import create_app

app = create_app()  # Call the function to create the app object

if __name__ == "__main__":
    app.run(debug=True)  # Run the app with debugging enabled
