from flask import render_template, url_for, request
from app.models import Product
from app import app

@app.route('/')
def index():
    caneca = Product(1, 'app/static/img/dummy.jpeg', 'Caneca', 1, 'Caneca Lorem Ipsum');
    camiseta = Product(2, 'app/static/img/dummy.jpeg', 'Camiseta', 10, 'Camiseta Lorem Ipsum');
    caixa = Product(3, 'app/static/img/dummy.jpeg', 'Caixa', 1.99, 'Caixa Lorem Ipsum');
    sacola = Product(4, 'app/static/img/dummy.jpeg', 'Sacola', 1.97, 'Sacola Lorem Ipsum');
    products = [caneca, camiseta, caixa, sacola];
    return render_template('index.html', products=products)

@app.route('/buy')
def buy():
    product_id = request.args.get('id')
    product = Product(1, 'app/static/img/dummy.jpeg', 'Caneca', 1, 'Caneca Lorem Ipsum');
    return render_template('buy.html', product=product)
