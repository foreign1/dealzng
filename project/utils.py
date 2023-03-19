from . import db
from .models import ShopItem

def get_items(page):
    items_per_page = 16
    items = ShopItem.query.paginate(page=page, per_page=items_per_page, error_out=False)
    return items

def truncate(text, length):
    return text[0: length]
