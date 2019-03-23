from flask import render_template, url_for, request
from app import app, db
from app.models import Product, ImageWorker

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/buy', methods=['GET', 'POST'])
def buy():
    product_id = request.args.get('id')
    product = Product.query.filter_by(id=product_id).first()
    thumb = url_for('static', filename=f'img/{product.thumb}')

    if request.method == 'POST':
        text = request.form.get('text')
        thumb = f'temporary/{ImageWorker.customize(product, text)}'

    return render_template('buy.html', product=product, thumb=thumb)
