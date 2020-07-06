from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

database = "./data/movements.db"
URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map?CMC_PRO_API_KEY={API_KEY}&symbol={currency}'
API_KEY='a8cf5d78-8dac-4325-838b-2ebe27f2f644'
currency = 'BTC,ETH,XRP,LTC,BCH,BNB,USDT,EOS,BSV,XLM,ADA,TRX'

def cryptos():
    conn = sqlite3.connect(database)
    cur = conn.cursor()

    cur.execute('''CREATE TABLE cryptos (id INTEGER PRIMARY KEY, name TEXT, symbol TEXT, slug TEXT)''')
    cur.execute("INSERT INTO cryptos VALUES ({}, {}, {}, {}).format('id','symbol','name', 'slug')")

    conn.commit()
    conn.close()


   
