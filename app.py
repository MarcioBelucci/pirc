from flask import Flask, render_template, abort
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

if __name__ == "__main__":
    app.run(debug=True)