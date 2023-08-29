"""
Module for main project and routes
"""
from flask import Flask, render_template, request
from src.app.nokia.facade import FacadeNokia
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
        data = request.form
        request_data = dict(
            olt_ip=data.get('olt_ip'),
            login_ssh=data.get('login_ssh'),
            ssh_pass=data.get('ssh_pass'),
            serial=data.get('serial')
            )
        response_request = FacadeNokia.search_onu(request_data)
        return render_template('search_onu.html',onu=response_request)
    