from flask import Blueprint, jsonify, request
import requests

# Erstellung eines Blueprint-Objekts mit dem Namen 'dragonball'
dragonball_bp = Blueprint('dragonball', __name__)

# Route für alle Charaktere
@dragonball_bp.route('/api/character/')
def get_characters():
    # URL zur API
    api_url = 'https://dbapidb.herokuapp.com/api/character/'
    response = requests.get(api_url)
    
    # Überprüfung der Antwort
    if response.status_code == 200:
        characters_data = response.json()
        return jsonify(characters_data)  # Rückgabe der Daten im JSON-Format
    else:
        return 'Fehler beim Abrufen der Daten.'

# Route für einen bestimmten Charakter anhand des Namens
@dragonball_bp.route('/api/character/<name>')
def get_single_character(name):
    name = name.replace(" ", "_")  # Formatierung des Namens für die API-Anfrage
    api_url = f'https://dbapidb.herokuapp.com/api/character/{name}'
    
    response = requests.get(api_url)
    
    # Überprüfung der Antwort und Rückgabe der Daten oder Fehlermeldung
    if response.status_code == 200:
        character_data = response.json()
        return jsonify(character_data)
    else:
        return "Charakter wurde nicht gefunden."

        