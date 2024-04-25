from app.db import connection
from json import loads, dumps

def indent_json(data):
    parsed = loads(data)
    r = dumps(parsed, indent=4) 
    return r

def get_all_locations():
    df_orders = connection.get_data_frame_gesemp('select * FROM locations')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_types():
    df_orders = connection.get_data_frame_gesemp('select * FROM contract_types')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_periods():
    df_orders = connection.get_data_frame_gesemp('select * FROM periods')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_concepts():
    df_orders = connection.get_data_frame_gesemp('select * FROM concepts')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_contracts():
    df_orders = connection.get_data_frame_gesemp('select * FROM contracts')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_releases():
    df_orders = connection.get_data_frame_gesemp('select * FROM releases')
    return indent_json(df_orders.to_json(orient = "table"))

def get_all_payrolls():
    df_orders = connection.get_data_frame_gesemp('select * FROM payrolls')
    return indent_json(df_orders.to_json(orient = "table"))