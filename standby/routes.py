from flask import Flask,render_template
import sqlite3
from requests.api import request

app = Flask(__name__)



@app.route('/purchase')

def compra():
    conn = sqlite3.connect(app.config['BASE_DATOS']) #conecto con fichero
    c = conn.cursor() #creo cursor
    query = ""
    
    

    datos = """(str('today.datetime'), str('now.datetime'), request.values.get('from_currency'),request.values.get('from_quantity'),
                request.values.get('to_currency'), request.values.get('to_quantity'),request.values.get('precio_unitario'))"""

    c.execute(query,datos) #ejecutamos la consulta    
    conn.commit() #grabo cambios
    conn.close()  #cierro conexion

    return render_template('purchase.html',datos)





@app.route("/status")
def status():
    conn = sqlite3.connect(app.config[]) #conecto con fichero #falta crear tabla cryptos
    c = conn.cursor() #creo cursor
    query ="SELECT symbol,price FROM movements "


    c.execute(query,invertido_en_euros,valor_actual)

    conn.commit() #grabo cambios
    conn.close()  #cierro conexion

def invertido_en_euros():
   # query = SELECT SUM (from_quantity=EUR) from movements
    #extraemos todos con EUR
    #INSERT INTO status SELECT sum
    #SELECT sum (quantity_to=EUR) esto redirect a API conversion

#def valor_actual():
    #query = (SELECT FROM currency 'todas los tipos de moneda')
    #SUM de from_quantity de moneda_from = moneda crypto cada linea para total por currency
   ## SUM de to_quantity de moneda_from = moneda crypto cada linea para total por currency

   # este resultado nos lleva a través de la API a total balance


@app.route("/inicio")
def datetime():
  today = datetime.date.fromtimestamp(time.time())
  now = datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, * , fold=0)

  d = []
  '''if d in datetime and 0 <= 'hour' > 24 and 0 <= 'minute'< 60 and 0 <= 'second' < 60 and 0 <= microsecond < 1000000
   and fold in [0, 1] and tzinfo=None '''
print ('today')
print ('now')






 



    

