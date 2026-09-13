from flask import Flask
from config import Config
from models import db, Product

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "ShopWise está no ar!"

if __name__ == "__main__":
    app.run(debug=True)