""" Importerer biblioteker vi trenger. """
from msilib.schema import Upgrade
import requests
import json

""" 
Dette er en rutine som skriver ut json objekter, brukes 
bare midlertidig for å se om ting fungere. """
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
""" Åpner jsonfila fra nett og gir den til ett objekt """
response = requests.get("http://api.open-notify.org/astros.json")

""" Komando for å skrive ut hele objektet. Midlertidig.
jprint(response.json()) """

""" Tar ut bare den den delen om people og lager ett nytt objekt med bare navn """
finnNavn= response.json()['people']

jprint (finnNavn)

""" Lager en tom liste som skal fylles. """
navn =[] 

""" Fyller opp lista etter hvor mange entries det er i objektet. """
for d in finnNavn:
    fulltNavn = d['name']
    navn.append(fulltNavn)

""" printer ut hele lista, denne er nå i pyhton format. """
print (navn)
