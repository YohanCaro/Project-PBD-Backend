from app.controller import query_orders
from flask import Blueprint

main = Blueprint('orders_blueprint',__name__)

@main.route("/orders/")
def get_orders():
    return query_orders.get_all_orders()

@main.route("/charges/")
def get_charges():
    return query_orders.get_all_charges()

@main.route("/contacts/")
def get_contacts():
    return query_orders.get_all_contacts()

@main.route("/suppliers/")
def get_suppliers():
    return query_orders.get_all_suppliers()

@main.route("/categories/")
def get_categories():
    return query_orders.get_all_categories()

@main.route("/products/")
def get_products():
    return query_orders.get_all_products()

@main.route("/shipping/")
def get_shipping():
    return query_orders.get_all_shipping()

@main.route("/customers/")
def get_customers():
    return query_orders.get_all_customers()

@main.route("/details/")
def get_details():
    return query_orders.get_all_details()