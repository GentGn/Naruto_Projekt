import requests

url = 'https://narutodb.xyz/api/character'  # Hier die URL deiner Flask-App-Routen einfügen

response = requests.get(url)

if response.status_code == 200:
    print(response.json()['characters'][0])  # Hier kannst du die Antwort anzeigen
else:
    print('Fehler bei der Anfrage:', response.status_code)
