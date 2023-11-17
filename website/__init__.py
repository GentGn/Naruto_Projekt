from flask import Flask  # Import der Flask-Klasse
from website.routes import dragonball_bp  # Import des Blueprint für Dragonball

def create_app():
  
    app = Flask(__name__)  # Erstellt eine Flask-Instanz

    app.register_blueprint(dragonball_bp)  # Registriert den Dragonball Blueprint

    return app  # Gibt die Flask-App zurück
