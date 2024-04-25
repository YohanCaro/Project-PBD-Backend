from app.db import connection
from json import loads, dumps

def indent_json(data):
    parsed = loads(data)
    r = dumps(parsed, indent=4) 
    return r

def get_all_orders():
    df_orders = connection.get_data_frame_orders('select * FROM orders')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_charges():
    df_orders = connection.get_data_frame_orders('select * FROM charges')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_contacts():
    df_orders = connection.get_data_frame_orders('select * FROM contacts')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_suppliers():
    df_orders = connection.get_data_frame_orders('select * FROM suppliers')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_categories():
    df_orders = connection.get_data_frame_orders('select * FROM categories')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_products():
    df_orders = connection.get_data_frame_orders('select * FROM products')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_shipping():
    df_orders = connection.get_data_frame_orders('select * FROM shipping_company')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_customers():
    df_orders = connection.get_data_frame_orders('select * FROM customers')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_details():
    df_orders = connection.get_data_frame_orders('select * FROM details_orders')
    return indent_json(df_orders.to_json(orient = "table"))

