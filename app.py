#! /usr/bin/env python

from os import environ
import sys
import signal
from pymongo import MongoClient
from flask import Flask, request, redirect, render_template, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    listaClientes=getNomesClientes()
    listaSolicitantes=getNomesSolicitantes()
    return render_template('main.jinja', listaClientes=listaClientes, listaSolicitantes=listaSolicitantes)
    #return render_template('main.jinja')
@app.route('/', methods=['POST'])

#Coloca dados do forms em formato json
def gravar():
    if database_enabled:
        form = json.dumps(request.form)
        db.forms.insert_one(form) #metodo maluco do pymongo
    return render_template('main.jinja', mensagem="Dados gravados na base com sucesso!")

#Puxar nome de clientes do BD em formato de searchlist. Nomes foram injetados no banco por meio da interface Web do Mongo
def getNomesClientes():
    if database_enabled:
        try:
            return [cliente for cliente in db.clientes.find()]
        except:
            return None
    else:
        return None
    
#Puxar nome de solicitantes do BD em formato de searchlist. Nomes foram injetados no banco por meio da interface Web do Mongo
def getNomesSolicitantes():
    if database_enabled:
        try:
            return [solicitante for solicitante in db.solicitantes.find()]
        except:
            return None
    else:
        return None


def sigterm_handler(_signo, _stack_frame):
    sys.exit(0)
    
#Conexão com o BD
if __name__ == '__main__':
    try:
        dbname = environ['database-name']
        dbuser = environ['database-user']
        dbpass = environ['database-password']
        client = MongoClient('mongodb://%s:%s@mongodb/%s' % (dbuser,dbpass,dbname))
        db = client[dbname]
        database_enabled = True
        print("Conexão OK!")
    except:
        database_enabled = False
        print("Conexão NOK!")

    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        app.run(host='0.0.0.0', port=8080)
    finally:
        print('Exiting...')
