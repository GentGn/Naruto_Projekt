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
        return render_template('all_characters_list.html', characters_all_names=characters_data)
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
            #print(character_data)  # Ausgabe der gesamten API-Antwort
            # Rest des Codes
            return render_template('search_results.html',  character_info=character_data )
        else:
            print('Fehler beim Abrufen der Daten:', response.status_code)
            return 'Fehler beim Abrufen der Daten. Bitte navigieren Sie zurück zur Startseite und überprüfen Ihre Eingabe.'
    else:
        return redirect(url_for('naruto.show_all_characters'))
    

@naruto_bp.route('/clans')
def get_clans():
    api_url = 'https://narutodb.xyz/api/clan?page=1&limit=1500'
    response = requests.get(api_url)

    if response.status_code == 200:
        clan_data = response.json()
        #print(clan_data)  # Ausgabe der gesamten API-Antwort
        return render_template('clans_list.html', clan_info=clan_data)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)
        return 'Fehler beim Abrufen der Daten für die Clans.'

@naruto_bp.route('/kekkeigenkai')
def get_kekkeigekai():
    api_url = 'https://narutodb.xyz/api/kekkei-genkai?page=1&limit=1500'
    response = requests.get(api_url)

    if response.status_code == 200:
        kekkeigenkai_data = response.json()
        return render_template('kekkeigenkai_list.html', kekkeigenkai_info=kekkeigenkai_data)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)
        return 'Fehler beim Abrufen der Daten für die Kekkeigenkais.'
    
@naruto_bp.route('/tailed_beasts')
def get_tailed_beast():
    api_url = 'https://narutodb.xyz/api/tailed-beast?page=1&limit=1500'
    response = requests.get(api_url)

    if response.status_code == 200:
        tailed_beast_data = response.json()
        return render_template('tailed_beasts_list.html', tailed_beasts_info=tailed_beast_data)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)
        return 'Fehler beim Abrufen der Daten für die Bijus.'
    
@naruto_bp.route('/villages')
def get_villages():
    api_url = 'https://narutodb.xyz/api/village?page=1&limit=1500'
    response = requests.get(api_url)

    if response.status_code == 200:
        village_data = response.json()
        return render_template('village_list.html', villages_info=village_data)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)
        return 'Fehler beim Abrufen der Daten für die Dörfer.'
    
@naruto_bp.route('/teams')
def get_teams():
    api_url = 'https://narutodb.xyz/api/team?page=1&limit=1500'
    response = requests.get(api_url)

    if response.status_code == 200:
        teams_data = response.json()
        return render_template('team_list.html', teams_info=teams_data)
    else:
        print('Fehler beim Abrufen der Daten:', response.status_code)
        return 'Fehler beim Abrufen der Daten für die Dörfer.'