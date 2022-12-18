
from flask import Flask, render_template
from turbo_flask import Turbo
import threading
import random
import re
import time

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

@app.context_processor
def inject_load():
    load = [int(random.random() * 100) / 100 for _ in range(3)]
    return {'load1': load[0], 'load5': load[1], 'load15': load[2]}
