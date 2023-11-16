from flask import Blueprint, jsonify, request
import requests

dragonball_bp = Blueprint('dragonball', __name__)

@dragonball_bp.route('/api/character/')
def get_characters():
    api_url = 'https://dbapidb.herokuapp.com/api/character/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        characters_data = response.json()
        return jsonify(characters_data)
    else:
        return 'Fehler beim Abrufen der Daten.'

@dragonball_bp.route('/api/character/<name>')
def get_single_character(name):
    name = name.replace(" ", "_")
    api_url = f'https://dbapidb.herokuapp.com/api/character/{name}'
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        character_data = response.json()
        return jsonify(character_data)
    else:
        return "Charakter wurde nicht gefunden."

   


        