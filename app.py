from flask import Flask, render_template
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    product_list = Product.query.all()
    return render_template("index.html", products=product_list)
    

if __name__ == "__main__":
    app.run(debug=True)