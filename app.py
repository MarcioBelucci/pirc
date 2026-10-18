from flask import Flask, render_template, abort, request
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    product_list = Product.query.all()
    return render_template("index.html", products=product_list)

@app.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get(product_id)
    if product is None:
        abort(404)
    return render_template("product_detail.html", product=product)

@app.route("/compare")
def compare():
    ids = request.args.getlist("ids")
    try:
        product_ids = set([int(parte) for item in ids for parte in item.split(",")])
    except ValueError:
        abort(400)
    if not 2 <= len(product_ids) <= 3:
        abort(400)
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    return render_template("compare.html", products=products)

if __name__ == "__main__":
    app.run(debug=True)