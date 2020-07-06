from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
   conn = sqlite3.connect(app.config['data/movements.db'])  #conecto
   cursor_operations = conn.cursor() #creo cursor tabla operations
   query = """ INSERT INTO operations('date', 'time', 'from_currency', 'from_quantity', 'to_currency', 'to_quantity')
               VALUES (?, ?, ?, ?, ?, ? );"""  #consulta

   conn.commit()
   conn.close()
   
   registros = []
   d = {}
   for dataRow in registros:
      print(dataRow)
   
   

      return render_template('index.html')
      return dataRow

@app.route("/purchase", methods =['GET','POST'])
def purchase():
   crypto = request.values['from_currency']

   conn = sqlite3.connect(app.config['data/movements.db'],)  #conecto
   cursor_operations = conn.cursor() #creo cursor tabla operations
   query = """  INSERT INTO operations('date', 'time', 'from_currency', 'from_quantity', 'to_currency', 'to_quantity')
               VALUES (?, ?, ?, ?, ?, ? ); """  #consulta
   
   #from_currency = linea[3]
   #from_quantity = linea[4]
   #to_currency = linea [5]
   #to_quantity = linea[6]

   
   cursor_operations.execute(query)
   
   
   conn.commit()
   conn.close()

   return render_template('purchase.html')  
   

@app.route("/status")
def status():
   return render_template('status.html')