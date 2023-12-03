"""Aplicação para visualização de perfil GitHub"""
from flask import Flask, render_template, request
import requests, json, pprint

app = Flask(__name__)

@app.route('/')
def index():
    '''Index page.''' 
    return render_template("index.html")
@app.route('/', methods=["POST"])
def get_username():
    '''Profile page.'''
    user = request.form['user']
    resposta = requests.get(f'https://api.github.com/users/{user}',headers={'Accept': 'application/json'},timeout=10)
    body = resposta.json()

    return render_template("pass.html", dado=body)
