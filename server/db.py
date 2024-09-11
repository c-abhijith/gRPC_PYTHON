
items_db = {}  

def add_item(item):
    items_db[item.id] = item

def get_item(item_id):
    return items_db.get(item_id)

def update_item(item):
    items_db[item.id] = item

def delete_item(item_id):
    return items_db.pop(item_id, None)

def list_items():
    return list(items_db.values())
