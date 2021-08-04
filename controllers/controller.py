from app import app
from flask import render_template
from models.orders import *

@app.route('/')
def index():
    return "Hello guys"