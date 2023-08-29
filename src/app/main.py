"""
Module for main project and routes
"""
from flask import Flask, render_template

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
