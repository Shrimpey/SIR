
from flask import Flask, render_template
from turbo_flask import Turbo
import threading
import random
import re
import time
import serial

app = Flask(__name__)
turbo = Turbo(app)

@app.before_first_request
def before_first_request():
    threading.Thread(target=update_load).start()

def update_load():
    with app.app_context():
        while True:
            time.sleep(2)
            turbo.push(turbo.replace(render_template('data.html'), 'data'))

@app.route('/')
def index():
    return render_template('index.html')

data1 = "No data"
data2 = "No data"
data3 = "No data"
data4 = "No data"
data5 = "No data"

@app.context_processor
def inject_load():
    com = serial.Serial("/dev/serial0", 115200)
    data = str(com.readline())
    splitdata = data.split("(")[1]
    data1temp = splitdata.split(",")[0]
    data2temp = splitdata.split(",")[1]
    data3temp = splitdata.split(",")[2]
    data4temp = splitdata.split(",")[3]
    data5temp = splitdata.split(",")[4].split(")")[0]

    if data1temp != "nan":
        data1 = data1temp
    if data2temp != "nan":
        data2 = data2temp
    if data3temp != "nan":
        data3 = data3temp
    if data4temp != "nan":
        data4 = data4temp
    if data5temp != "nan":
        data5 = data5temp

    return {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5}
