from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from . import db
from .utils import get_items

main = Blueprint('main', __name__)

@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    items = get_items(page)
    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if items.has_next else None
    return render_template('index.html', shopitems=items.items, has_prev=items.has_prev,
                           has_next=items.has_next, prev_num=prev_page, next_num=next_page, current_user=current_user)
