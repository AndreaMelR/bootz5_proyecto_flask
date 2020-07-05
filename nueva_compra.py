from flask import Flask,render_template
import sqlite3

app = Flask(__name__)


@app.route("/purchase", methods=['GET','POST'])
def compras():
    conn = sqlite3.connect(app.config['BASE_DATOS'])
    c = conn.cursor()
    query = "SELECT symbol, price FROM movements;"
    movements = c.execute(query).fetchall()
    
    conn.close()



    return render_template('purcahse.html',movements)   #revisar
