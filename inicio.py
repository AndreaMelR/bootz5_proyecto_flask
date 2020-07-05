from flask import Flask,render_template
import sqlite3
from requests.api import request

app = Flask (__name__)

@app.route ("/")
def index():
    conn = sqlite3.connect(app.config['BASE_DATOS']) #conecto con fichero
    c = conn.cursor() #creo cursor y lo  meto en variable c
    query = """ INSERT INTO movements (date, time, from_currency, from_quantity, to_currency, to_quantity)
                            VALUES ({}', '{}:00.000000', '{}', '{}', '{}', '{}');"""
    f = request.values #tomamos los datos de entrada del formulario
    query = query.format(f['date'], f['time'], f['from_currency'], f['from_quantity'], f['to_currency'], f['to_quantity'])#construimos consulta como una cadena
   
    conn.commit() #grabo cambios
    conn.close()  #cierro conexion
   
    movements = []
    data = {} #diccionario con registros
    for fila in movements:
        movements.append(fila)
        if fila[0] in data:
            data[fila[0]]['from_currency'] += float(fila[4])           
        else:
            if fila[0] != 'from_currency':
                data[fila[0]] = {'from_curency': float(fila[4])}
        
    return render_template('index.html',movimientos=data)