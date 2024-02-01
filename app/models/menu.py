# app/models/menu.py

from .. import db

class ItemCardapio(db.Model):
    __tablename__ = 'itens_cardapio'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(50), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(250), nullable=True)
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Item {self.nome}>'
