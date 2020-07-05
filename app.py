from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
   conn = sqlite3.connect(app.config['DATA_BASE'])  #conecto
   cur = conn.cursor() #creo cursor
   query = """ INSERT INTO operations('date', 'time', 'from_currency', 'from_quantity', 'to_currency', 'to_quantity')
               VALUES (?, ?, ?, ?, ?, ? );"""  #consulta
   
   registros = []
   dataRow = {}
   for dataRow in registros:
      datos = (dataRow[1], dataRow[2], dataRow[3], dataRow[4], dataRow[5], dataRow[6])
      cur.execute(query, datos)
   
   conn.commit()
   conn.close()

   return render_template('index.html',registros)

#try:
#   pass
#except (ConnectionError, TimeoutError) as e:
 #  print (e) 


@app.route("/purchase", methods =['GET','POST'])

def new_purchase():
   request.form
   ##From = request.values['currency']
   #currency = ('EUR','BTC')
   #amount = ""

   #for symbol in currency and amount != 0:
    #  symbol = float(currency)
   
   #else:
    #  pass

   return render_template('purchase.html')

@app.route("/status")
def status():
   return render_template('status.html')