from flask import render_template, url_for, request
from app import app
from app.models import Product

@app.route('/')
def index():
    caneca = Product(1, url_for('static', filename='img/dummy.jpeg'), 'Caneca', 1, 'Caneca Lorem Ipsum');
    camiseta = Product(2, url_for('static', filename='img/dummy.jpeg'), 'Camiseta', 10, 'Camiseta Lorem Ipsum');
    caixa = Product(3, url_for('static', filename='img/dummy.jpeg'), 'Caixa', 1.99, 'Caixa Lorem Ipsum');
    sacola = Product(4, url_for('static', filename='img/dummy.jpeg'), 'Sacola', 1.97, 'Sacola Lorem Ipsum');
    products = [caneca, camiseta, caixa, sacola];
    return render_template('index.html', products=products)

@app.route('/buy')
def buy():
    product_id = request.args.get('id')
    product = Product(1, url_for('static', filename='img/dummy.jpeg'), 'Caneca', 1, 'WHY???');
    return render_template('buy.html', product=product)
