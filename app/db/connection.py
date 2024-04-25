from sqlalchemy import create_engine
from decouple import config
import pandas as pd

engine_rh = create_engine(config('ORACLE_DB_RH'))

engine_or = create_engine(config('ORACLE_DB_ORDERS'))

engine_ge = create_engine(config('ORACLE_DB_GE'))

def get_data_frame_orders(query):
    try:
        return pd.read_sql_query(query, engine_or)
    except Exception as ex:
        print(ex)

def get_data_frame_gesemp(query):
    try:
        return pd.read_sql_query(query, engine_ge)
    except Exception as ex:
            print(ex)

def get_data_frame_rh(query):
    try:
        return pd.read_sql_query(query, engine_rh)
    except Exception as ex:
        print(ex)

