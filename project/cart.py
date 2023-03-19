from flask import Blueprint, render_template, request, jsonify, redirect, url_for, flash, current_app
from flask_login import login_required, current_user
from . import db
from .models import User, ShopItem, Cart, CartItem
from flask_mail import Message
from . import mail

cart = Blueprint('cart', __name__)

@cart.route('/cart', methods=['GET'])
@login_required
def my_cart():
    cart = current_user.cart

    if not cart:
        flash('Your cart is empty, browse to add items to cart first!')
        return redirect(url_for('main.index'))
    
    cart_items = []
    cart_total = 0
    for cart_item in cart[0].items:
        si = ShopItem.query.filter_by(id=cart_item.item_id).first()
        cart_items.append({
            'cart_item_id': cart_item.id,
            'name': si.name,
            'category': si.category,
            'price_actual': si.price,
            'price_discount': si.discount_price
        })

        cart_total += si.discount_price

    return render_template('cart.html', cart=cart_items, cart_total=cart_total)

@cart.route('/add_to_cart', methods=['GET'])
@login_required
def add_to_cart():
    item_id = request.args.get('item_id')

    # Check if the current user has an existing cart
    cart = Cart.query.filter_by(user_id=current_user.id).first()

    # If there is no existing cart, create a new cart object
    if not cart:
        cart = Cart(user_id=current_user.id)
        db.session.add(cart)
        db.session.commit()

    # Create a new cart item with the given item_id and add it to the cart
    cart_item = CartItem(item_id=item_id, cart_id=cart.id)
    db.session.add(cart_item)
    db.session.commit()

    flash('Item added to cart successfully!')
    return redirect(url_for('main.index'))

@cart.route('/delete_item', methods=['GET'])
@login_required
def delete_item():
    cart_item_id = request.args.get('cart_item_id')
    cart_item = CartItem.query.filter_by(id=cart_item_id).first()

    if cart_item:
        db.session.delete(cart_item)
        db.session.commit()
        flash('Item deleted from cart successfully!')
    else:
        flash('Item not found in cart.')

    return redirect(url_for('cart.my_cart'))

@cart.route('/make_payment', methods=['POST'])
@login_required
def make_payment():
    number = request.form.get('number')
    cvv = request.form.get('cvv')
    exp = request.form.get('exp')
    pin = request.form.get('pin')

    if not number or not cvv or not exp or not pin:
        flash('All specified card information are required!')
        return redirect(url_for('cart.my_cart'))

    # get the user's cart items
    cart_items = CartItem.query.filter_by(cart_id=current_user.cart[0].id).all()

    # create a list of items with their name and price_discount
    items = []
    total = 0
    for item in cart_items:
        shop_item = ShopItem.query.filter_by(id=item.item_id).first()
        item_info = {
            'name': shop_item.name,
            'price_discount': shop_item.discount_price
        }
        items.append(item_info)
        total += shop_item.discount_price

    purchases = '\n'
    for item in items:
        name = item['name']
        price = item['price_discount']
        purchases += f'{name}: {price}\n'

    msg = Message(f'Hello {current_user.name}', sender=current_app.config['MAIL_USERNAME'], recipients=[current_user.email])
    msg.body = msg.body = f"Hello, \nYour payment of {total} was successful. \nHere is your cart summary: {purchases}The total is: {total}."
    mail.send(msg)

    # clear cart
    for item in cart_items:
        db.session.delete(item)
    db.session.commit()

    flash('Payment processed successfully! You will receive a notification in your email!')
    return redirect(url_for('main.index'))
