import requests as r
from bs4 import BeautifulSoup as bs

with open('21millones.txt', 'r', encoding='cp1252') as f:
    data = f.read()
with open('22millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()

counter = 0 
data = data.split('\n')
for linea in data:
    if linea.startswith('OCTAVIA') and 'CAMINO' in linea :
        linea = linea.split(',')
        rut = linea[1]
        busqueda = r.get(f'https://www.google.com/search?client=firefox-b-d&q={rut}')
        soup = bs(busqueda.text, 'html.parser')
        print(soup.get_text())

        counter += 1

print(f'se encontraron {counter}')

