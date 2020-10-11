#! /usr/bin/env python

from os import environ
import sys
import signal
from pymongo import MongoClient
from flask import Flask, request, redirect, render_template, json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def inicio():
    #llistaClientes=getNomesClientes()
    #listaSolicitantes=getNomesSolicitantes()
    #return render_template('main.jinja', listaClientes=listaClientes, listaSolicitantes=listaSolicitantes)
    return render_template('main.jinja')
@app.route('/', methods=['POST'])
def gravar():
    if database_enabled:
        form = request.form.to_dict()
        db.forms.insert_one(form)
    return redirect('/')

def getNomesClientes():
    if database_enabled:
        try:
            return [cliente for cliente in db.clientes.find()]
        except:
            return None
    else:
        return None

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
