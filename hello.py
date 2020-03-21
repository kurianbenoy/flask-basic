from flask import Flask

import requests
app = Flask(__name__)

@app.route('/hello/')
def hello_world():
    return ('Hello, World!')

@app.route('/india_covid/', methods=['GET','POST'])
def no_case():
    r = requests.get('https://covid19indiaapi.herokuapp.com/v1/overall')
    return r.json()