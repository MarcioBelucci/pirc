from app import app, db
from models import Product

produtos_mock = [
    {"name": "Samsung A21 5G", "price": 1200, "category": "phone", "score": 4.5, "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Non atque, ratione ipsum consequatur hic excepturi natus dolores enim suscipit temporibus, nam vitae vel fugiat magni, aperiam sint nihil voluptatum vero."},
    {"name": "Iphone 18 Pro", "price": 8000, "category": "phone", "score": 4.8, "description": "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore optio eos non nihil harum ut magnam ullam illo rerum, dolores, temporibus ex neque. Eius quam dolor, saepe iste deleniti provident."},
    {"name": "Teclado Valheim Redragon - Swich Brown", "price": 200, "category": "keyboard", "score": 4.2, "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Harum blanditiis mollitia facere quia impedit laborum repellendus obcaecati aut minus hic assumenda, excepturi sed ex, aspernatur labore fuga dolor et quibusdam!"},
    {"name": "Playstation 5 Slim", "price": 4500, "category": "videogame", "score": 4.7, "description": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Rem, et? Consequuntur doloribus maiores quae enim, delectus temporibus deleniti itaque excepturi eligendi officiis, nam nemo incidunt deserunt illum commodi accusantium asperiores?"},
]

with app.app_context():
    for dados in produtos_mock:
        produto = Product(**dados)
        db.session.add(produto)
    db.session.commit()
    print(f"{len(produtos_mock)} produtos inseridos com sucesso!")