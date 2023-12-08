# -*- coding: utf-8 -*-
from flask import Flask  # Import der Flask-Klasse
from website.routes import naruto_bp  # Import des Blueprint für Dragonball

def create_app():
  
    app = Flask(__name__)  # Erstellt eine Flask-Instanz

    app.register_blueprint(naruto_bp)  # Registriert den Naruto Blueprint

    return app  # Gibt die Flask-App zurück
