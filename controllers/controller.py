from app import app
from flask import render_template
from models.orders import *

@app.route('/orders')
def index():
    return render_template('index.html', orders = orders_list)

@app.route("/orders/<num>")
def order(num):
    return render_template('order.html', order = orders_list[int(num)])