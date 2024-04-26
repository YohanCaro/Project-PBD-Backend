from app.db import connection
from json import loads, dumps, load
import os
import pandas as pd

def indent_json(data):
    parsed = loads(data)
    r = dumps(parsed, indent=4) 
    return r
"""
Cantidad de pedidos realizados en los distintos años / muestra las ordenes
Return: return datatable in json
"""
def get_first_query(filter):
    df_o = connection.get_data_frame_orders('select * FROM orders')
    df_o = df_o[df_o['order_date'].dt.month == int(filter)]
    df_o['month'] = df_o['order_date'].dt.month_name()
    df_res = df_o.filter(items=['month','id_order'])
    df_res = df_res.rename(columns={'month':'Mes', 'id_order':'Pedido'})
    df_res = df_res.reset_index(drop=True)
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de pedidos por forma de pago.
Return: return datatable in json
"""
def get_second_query(filter):
    df_o = connection.get_data_frame_orders('select * FROM orders')
    df_o = df_o[(df_o['order_date'].dt.year == int(filter))]
    df_o = df_o.replace('E', value='Efectivo')
    df_o = df_o.replace('C', value='Tarjeta de Crédito')
    df_res = df_o[['payment_method', 'id_order']].groupby(['payment_method']).count()
    df_res = df_res.rename(columns={'id_order':'Cantidad Pedidos'})
    df_res.index.names = ['Producto']
    return indent_json(df_res.to_json(orient = "table"))

"""
10 productos mas vendidos
"""
def get_third_query(filter):
    df_or= connection.get_data_frame_orders('select id_product, quantity_d_o FROM details_orders')
    df_pro = connection.get_data_frame_orders('select id_product, product_name FROM products')
    df_res = pd.merge(df_or, df_pro, how='left', on='id_product')
    df_res = df_res.filter(items=['product_name', 'quantity_d_o']).groupby(['product_name']).sum()
    df_res['Rank'] = df_res['quantity_d_o'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.rename(columns={'quantity_d_o':'Cantidad Productos'})
    df_res.index.names = ['Producto']
    return indent_json(df_res.head(int(filter)).to_json(orient = "table"))

"""
Top ordenes más costosas
Return: return datatable in json
"""
def get_fourth_query(filter):
    df_o = connection.get_data_frame_orders('select id_order,send_value from orders')
    df_d = connection.get_data_frame_orders('select id_order,price_unit,quantity_d_o,discount_d_o from details_orders')
    df_res = pd.merge(df_o, df_d, how='left', on='id_order')
    df_res['Total'] = df_res['send_value'] + ((df_res['price_unit']*df_res['quantity_d_o']) +
                      (df_res['price_unit']*df_res['quantity_d_o'])*df_res['discount_d_o'])
    df_res['Rank'] = df_res['Total'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.filter(items=['id_order','total','rank'])
    df_res = df_res.rename(columns={'id_order':'Pedido'})
    df_res = df_res.reset_index(drop=True)
    return indent_json(df_res.head(int(filter)).to_json(orient = "table"))

"""
Top ordenes menos costosas
Return: return datatable in json
"""
def get_fifth_query(filter):
    df_o = connection.get_data_frame_orders('select id_order,send_value from orders')
    df_d = connection.get_data_frame_orders('select id_order,price_unit,quantity_d_o,discount_d_o from details_orders')
    df_res = pd.merge(df_o, df_d, how='left', on='id_order')
    df_res['Total'] = df_res['send_value'] + ((df_res['price_unit']*df_res['quantity_d_o']) +
                      (df_res['price_unit']*df_res['quantity_d_o'])*df_res['discount_d_o'])
    df_res['Rank'] = df_res['Total'].rank(method='max')
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.filter(items=['id_order','Total','quantity_d_o','Rank'])
    df_res = df_res.rename(columns={'id_order':'Pedido','quantity_d_o':'Cantidad'})
    df_res = df_res.reset_index(drop=True)
    return indent_json(df_res.head(int(filter)).to_json(orient = "table"))

"""
Cantidad de productos por proveedor (sin contar en stock)
Return: return datatable in json
"""
def get_sixth_query(filter):
    df_p = connection.get_data_frame_orders('select * from products')
    df_s = connection.get_data_frame_orders('select * from suppliers')
    df_res = pd.merge(df_p,df_s, how='left', on='id_supplier')
    df_res = df_res.filter(items=['company_name', 'id_product']).groupby(['company_name']).sum()
    df_res['Rank'] = df_res['id_product'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.rename(columns={'id_product':'Cantidad'})
    df_res.index.names = ['Proveedor']
    return indent_json(df_res.head(int(filter)).to_json(orient = "table"))

"""
Cantidad de productos por proveedor (contando en stock)
Return: return datatable in json
"""
def get_seventh_query(filter):
    df_p = connection.get_data_frame_orders('select * from products')
    df_s = connection.get_data_frame_orders('select * from suppliers')
    df_res = pd.merge(df_p,df_s, how='left', on='id_supplier')
    df_res = df_res.filter(items=['company_name', 'units_in_stock']).groupby(['company_name']).sum()
    df_res['rank'] = df_res['units_in_stock'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['rank'])
    df_res = df_res.rename(columns={'company_name':'Proveedor','units_in_stock':'Cantidad'})
    df_res.index.names = ['Proveedor']
    return indent_json(df_res.head(int(filter)).to_json(orient = "table"))

"""
Productos vencidos por mes en el año 2022
Return: return datatable in json
"""
def get_eighth_query(filter):
    df_p = connection.get_data_frame_orders('select * from products')
    df_p['exp_month'] = df_p['expiration_date'].dt.month_name()
    df_p = df_p[(df_p['expiration_date'].dt.month == int(filter))]
    df_res = df_p.filter(items=['product_name', 'exp_month'])
    df_res = df_res.rename(columns={'product_name':'Producto','exp_month':'Mes'})
    df_res = df_res.reset_index(drop=True)
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de ordenes realizadas por compañia de envios
Return: return datatable in json
"""
def get_ninth_query():
    df_o = connection.get_data_frame_orders('select * from orders')
    df_s = connection.get_data_frame_orders('select * from shipping_company')
    df_join = pd.merge(df_o,df_s, how='left', on='id_shipping_company')
    df_res = df_join.filter(items=['shipping_company_name', 'id_order']).groupby(['shipping_company_name']).count()
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de ordenes realizadas por compañia de envios por mes
Return: return datatable in json
"""
def get_tenth_query(filter):
    df_o = connection.get_data_frame_orders('select * from orders')
    df_s = connection.get_data_frame_orders('select * from shipping_company')
    df_res = pd.merge(df_o,df_s, how='left', on='id_shipping_company')
    df_res = df_res[(df_res['shipping_company_name'] == filter)]
    df_res['delivery_year'] = df_res['delivery_date'].dt.year
    df_res['delivery_month'] = df_res['delivery_date'].dt.month
    df_res = pd.pivot_table(df_res, values=('id_order'), index=['delivery_year'], columns=['delivery_month'], aggfunc="count")
    df_res = rename(df_res)
    return indent_json(df_res.to_json(orient = "table"))

def get_descriptions_json():
    SITE_ROOT = os.path.realpath(os.path.dirname('app'))
    json_url = os.path.join(SITE_ROOT, "static\\","description_queries.json")
    data = load(open(json_url))
         
    return data

def rename(daf):
    daf = daf.rename(columns={1:'January'})
    daf = daf.rename(columns={2:'February'})
    daf = daf.rename(columns={3:'March'})
    daf = daf.rename(columns={4:'April'})
    daf = daf.rename(columns={5:'May'})
    daf = daf.rename(columns={6:'June'})
    daf = daf.rename(columns={7:'July'})
    daf = daf.rename(columns={8:'August'})
    daf = daf.rename(columns={9:'September'})
    daf = daf.rename(columns={10:'October'})
    daf = daf.rename(columns={11:'November'})
    daf = daf.rename(columns={12:'December'})
    return daf