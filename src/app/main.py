"""
Module for main project and routes
"""
from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='../templates',
            static_url_path='/static',
            static_folder='../static'
            )

@app.route('/')
def index():
    """
    Main webpage
    """
    return render_template('index.html')

@app.route('/buscar_onu',methods=['POST','GET'])
def search_onu():
    """
    Search ONU Method for render webpage
    """
    if request.method == 'GET':
        return render_template('search_onu.html')
    if request.method == 'POST':
        print("Chegou post aqui")
        return render_template('search_onu.html',onu="To aqui")
    