from app.controller import query_gesemp
from flask import Blueprint

main = Blueprint('ge_blueprint',__name__)

@main.route("/locations")
def get_locations():
    return query_gesemp.get_all_locations()

@main.route("/contracts")
def get_contracts():
    return query_gesemp.get_all_contracts()

@main.route("/types")
def get_types():
    return query_gesemp.get_all_types()

@main.route("/periods")
def get_periods():
    return query_gesemp.get_all_periods()

@main.route("/concepts")
def get_concepts():
    return query_gesemp.get_all_concepts()

@main.route("/releases")
def get_releases():
    return query_gesemp.get_all_releases()

@main.route("/payrolls")
def get_payrolls():
    return query_gesemp.get_all_payrolls()