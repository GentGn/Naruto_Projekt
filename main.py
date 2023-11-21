from website import create_app
from website.routes import naruto_bp


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, port=3001)
