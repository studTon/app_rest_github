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
    '''Página de perfil que mostra as informações públicas do usuário.
    As informações são processadas numa sequência para avaliar as estatísticas.'''

    user = request.form['user']
    resposta = requests.get(
        f'https://api.github.com/users/{user}',
        headers={'Accept': 'application/json'},
        timeout=10)
    body = json.loads(resposta.text)
    nome = body['name']
    conta = body['login']
    biografia = body['bio']
    local = body['location']
    repositorios = body['public_repos']
    n_seguidores = body['followers']
    n_conexoes = body['following']

    return render_template("pass.html", 
                           name=nome,
                           login=conta,
                           bio=biografia,
                           location=local,
                           repos=repositorios,
                           followers=n_seguidores,
                           following=n_conexoes)
