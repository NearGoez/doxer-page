from flask import Blueprint, render_template, request
import time

with open('website/18millones.txt', 'r', encoding='cp1252') as f:
    data = f.read()
with open('website/19millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/20millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/21millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/22millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/23millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/24millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/25millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/26millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()
with open('website/27millones.txt', 'r', encoding='cp1252') as f:
    data += f.read()

data = data.split('\n')

def buscar(nombres, apellidos):
    nombres, apellidos = nombres.upper(), apellidos.upper()
    resultado = '<html><body><p>'
    for x in data:
        if nombres in x and apellidos in x:

            resultado += f'{x} <br>'

    
    resultado += '</p></body></html>'
    return resultado

views = Blueprint("views", __name__)

@views.route('/')

def home():
    return render_template('index.html')

@views.route('/resultado', methods=['POST', 'GET'] )

def resultado():
    nombres = request.form.get('nombres')  
    apellidos = request.form.get('apellidos')
    if nombres == '' and apellidos =='' or (nombres==None and apellidos==None):
        return render_template('index.html')

    resultado = f'{nombres} {apellidos}'
    print(resultado)

    with open('reg.txt', 'a') as f:
        f.write(f'{resultado}\n')

    return buscar(nombres, apellidos)

    



