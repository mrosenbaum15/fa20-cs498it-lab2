from flask import Flask, render_template, request
import sqlite3
import pandas as pd
from scipy.stats import pearsonr

app = Flask(__name__)

@app.route("/")
def main():
   connection = sqlite3.connect('xbee.db')
   db = conn.cursor() # connect to local db
   db.execute("SELECT * FROM sensordata ORDER BY id DESC")
   readings = db.fetchall() # get all data
   df = pd.read_csv("sensordata.csv") # calculating coefficient!
   list1 =df["devices"]
   list2 =df["airquality"]
   corr,_ = pearsonr(list1,list2)
   return render_template('home_page.html', data=data, corr=corr) # template for home_page.html
