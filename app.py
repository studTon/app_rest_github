"""Aplicação para visualização de perfil GitHub"""
import json
import requests
from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    '''Página inicial da aplicação.''' 
    return render_template("index.html")
@app.route('/', methods=["POST"])
def get_username():
    '''Página de perfil que mostra as informações públicas do usuário.'''
    user = request.form['user']
    resposta = requests.get(
        f'https://api.github.com/users/{user}',
        headers={'Accept': 'application/json'},
        timeout=10)
    body = resposta.json()
    return render_template("pass.html", dado=body)
