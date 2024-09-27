import requests
with open('/home/denis/webpage/website/18millones.txt', 'r', encoding='cp1252') as f:
    data = f.read()
with open('/home/denis/webpage/website/19millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/20millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/21millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/22millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/23millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/24millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/25millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/26millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('/home/denis/webpage/website/27millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()


data = data.split('\n')

def buscar(nombres= '', apellidos=''):

    nombres, apellidos = nombres.upper(), apellidos.upper()

    Pnombre = nombres.split(' ')
    Papellidos = apellidos.split(' ')


    resultado = ''

    for linea in data:
        if nombres in linea and apellidos in linea:
            persona = linea.split(',')[0].split(' ')
            ano = linea.split(',')[-2].split('/')[-1]
            rut = linea.split(',')[1].strip()

            #solicitud = requests.get(f'https://www.google.com/search?client=firefox-b-d&q={rut}').text
            

            if Pnombre[0] == persona[0] and (1995<=int(ano)<=2006) :
                resultado += f'{linea}\n'
    return resultado
print(buscar('octavia'))

print(requests.get('https://www.google.com/search?client=firefox-b-d&q=22100800-6').text)

