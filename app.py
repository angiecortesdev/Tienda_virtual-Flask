#imports

from flask import Flask, render_template, request, redirect, url_for, jsonify
import json, os

#application initialization
app = Flask(__name__)

DATA_FILE = 'products.json'

#route definition
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/agregar')
def agregar():
    return render_template('agregar.html')

#run the application

if __name__ == '__main__':
    app.run(debug=True)