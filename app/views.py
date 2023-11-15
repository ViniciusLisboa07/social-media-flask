from flask import Blueprint, render_template

main = Blueprint('main', __name__)

# app/views.py
from . routes import main

@main.route('/')
def index():
    return render_template('index.html')
