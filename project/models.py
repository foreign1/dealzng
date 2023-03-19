from enum import Enum
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func
from . import db

class CategoryChoices(str, Enum):
    TRAINING = "TRAINING"
    HOTEL = "HOTEL"
    TRAVEL = "TRAVEL"
    SPA = "SPA"
    RESTAURANT = "RESTAURANT"
    
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    cart = db.relationship('Cart', backref='user')

class ShopItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    category = db.Column(db.Enum(CategoryChoices))
    desc_short = db.Column(db.String(100))
    desc_long = db.Column(db.String(1000))
    price = db.Column(db.Float)
    discount_price = db.Column(db.Float)
    time_created = db.Column(db.DateTime(timezone=True), server_default=func.now())
    image = db.Column(db.String(200))

    def __init__(self, name, category, desc_short, desc_long, price, discount_price, time_created):
        self.name = name
        self.category = category
        self.desc_short = desc_short
        self.desc_long = desc_long
        self.price = price
        self.discount_price = discount_price
        self.time_created = time_created
        self.image = self._derive_image()

    def _derive_image(self):
        if self.category == CategoryChoices.TRAVEL:
            return 'travel.jpg'
        elif self.category == CategoryChoices.RESTAURANT:
            return 'restaurant.jpg'
        elif self.category == CategoryChoices.SPA:
            return 'spa.jpg'
        elif self.category == CategoryChoices.TRAINING:
            return 'training.jpg'
        elif self.category == CategoryChoices.HOTEL:
            return 'hotel.jpg'
        else:
            return 'hero.jpg'
        
class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    items = db.relationship('CartItem', backref='cart', lazy=True)

    def add_item(self, item):
        cart_item = CartItem.query.filter_by(item_id=item.id, cart_id=self.id).first()
        if cart_item:
            cart_item.quantity += 1
        else:
            cart_item = CartItem(item_id=item.id, cart_id=self.id, quantity=1)
            db.session.add(cart_item)
        db.session.commit()

    def remove_item(self, item):
        cart_item = CartItem.query.filter_by(item_id=item.id, cart_id=self.id).first()
        if cart_item:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
            else:
                db.session.delete(cart_item)
            db.session.commit()

    def get_total_cost(self):
        return sum([item.get_total_cost() for item in self.items])

class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('shop_item.id'), nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)

    def get_total_cost(self):
        return self.quantity * self.item.price

