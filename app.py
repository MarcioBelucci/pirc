from flask import Flask, render_template, abort, request
from config import Config
from models import db, Product
from scoring import price_score, final_score, PROFILES

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
    profile = request.args.get("profile", "balanced")
    if profile not in PROFILES:
        abort(400)
    try:
        product_ids = set([int(parte) for item in ids for parte in item.split(",")])
    except ValueError:
        abort(400)
    if not 2 <= len(product_ids) <= 3:
        abort(400)
    products = Product.query.filter(Product.id.in_(product_ids)).all()
    if len(products) != len(product_ids):
        abort(404)
    lowest_price = min(p.price for p in products)
    highest_price = max(p.price for p in products)
    price_scores = {}
    final_scores = {}
    for product in products:
        price_scores[product.id] = price_score(product.price, lowest_price, highest_price)
        final_scores[product.id] = final_score(price_scores[product.id], product.score, profile)
    return render_template("compare.html", products=products, price_scores=price_scores, final_scores=final_scores)

if __name__ == "__main__":
    app.run(debug=True)