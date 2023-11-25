from flask import Blueprint, jsonify, request, render_template, redirect, url_for
import requests


# Flask Blueprint erstellen
naruto_bp = Blueprint('naruto', __name__)

# Route für die Startseite


@naruto_bp.route('/')
def index():
    return render_template('index.html')

# Route für die Character_List.html


@naruto_bp.route('/character_list.html')
def character_list():
    return render_template('character_list.html')

# Route, um alle Charakternamen abzurufen und in der Template anzuzeigen


@naruto_bp.route('/character')
def show_all_characters():
    api_url = 'https://narutodb.xyz/api/character?page=1&limit=1500'
    response = requests.get(api_url)
    print(response, flush=True)
    # Statuscode der API-Antwort anzeigen
    print("Status Code:", response.status_code, flush=True)

    if response.status_code == 200:
        # Charakterdaten aus der API als JSON extrahieren
        characters_data = response.json()['characters']
        # print(characters_data, flush=True)
        # Charakternamen an die Vorlage übergeben und rendern
        return render_template('character_list.html', characters_all_names=characters_data)
    else:
        return 'Fehler beim Abrufen der Daten.'


@naruto_bp.route('/search')
def search_characters():
    search_query = request.args.get('search_query')

    if search_query:
        api_url = f'https://narutodb.xyz/api/character/search?name={search_query}'
        response = requests.get(api_url)

        if response.status_code == 200:
            character_data = response.json()
            print(character_data)  # Ausgabe der gesamten API-Antwort
            # Rest des Codes
            return render_template('search_results.html',  character_info=character_data )
        else:
            print('Fehler beim Abrufen der Daten:', response.status_code)
            return 'Fehler beim Abrufen der Daten. Bitte navigieren Sie zurück zur Startseite und überprüfen Ihre Eingabe.'
    else:
        return redirect(url_for('naruto.show_all_characters'))

'''
# Route, um einen einzelnen Charakter abzurufen
@naruto_bp.route('/api/character/<name>')
def get_single_character(name):
    api_url = f'https://narutodb.xyz/api/character/{name}'
    response = requests.get(api_url)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        character_data = response.json()
        # Print der spezifischen Charakterdaten
        print("Character Data:", character_data)

        if name in character_data:
            single_character = character_data[name]
            return jsonify(single_character)
        else:
            print("Charakter wurde nicht gefunden.")
            return "Charakter wurde nicht gefunden."
    else:
        print("Fehler beim Abrufen der Daten.")
        return "Fehler beim Abrufen der Daten."
'''
