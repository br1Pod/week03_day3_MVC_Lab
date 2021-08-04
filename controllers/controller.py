from app import app
from flask import render_template
from models.orders import orders_list

@app.route('/')
def index():
    return render_template('index.html', orders = orders_list)