from app.db import connection
from json import loads, dumps
import os
import pandas as pd

def indent_json(data):
    parsed = loads(data)
    r = dumps(parsed, indent=4) 
    return r

"""
Cantidad de pedidos realizados en los distintos años
Return: return datatable in json
"""
def get_first_query():
    df_o = connection.get_data_frame_orders('select * FROM orders')
    df_o['year'] = df_o['order_date'].dt.year
    df_o['month'] = df_o['order_date'].dt.month
    df_o = df_o.filter(items=['month', 'id_order', 'year'])
    df_res = pd.pivot_table(df_o, values=('id_order'), index=['year'], columns=['month'], aggfunc="count")
    df_res = rename(df_res)
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de pedidos por forma de pago.
Return: return datatable in json
"""
def get_second_query():
    df_o = connection.get_data_frame_orders('select * FROM orders')
    df_o = df_o.replace('E', value='Efective')
    df_o = df_o.replace('C', value='Credit_Card')
    df_res = df_o[['payment_method', 'id_order']].groupby(['payment_method']).count()
    df_res = df_res.rename(columns={'id_order':'Cantidad_Pedidos'})
    df_res.index.names = ['Metodo_Pago']
    return indent_json(df_res.to_json(orient = "table"))

"""
10 productos mas vendidos
"""
def get_third_query():
    df_or= connection.get_data_frame_orders('select id_product, quantity_d_o FROM details_orders')
    df_pro = connection.get_data_frame_orders('select id_product, product_name FROM products')
    df_res = pd.merge(df_or, df_pro, how='left', on='id_product')
    df_res = df_res.filter(items=['product_name', 'quantity_d_o']).groupby(['product_name']).sum()
    df_res['Rank'] = df_res['quantity_d_o'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.rename(columns={'quantity_d_o':'Cantidad_Productos'})
    df_res.index.names = ['Producto']
    return indent_json(df_res.head(10).to_json(orient = "table"))

"""
Top ordenes más costosas
Return: return datatable in json
"""
def get_fourth_query():
    df_o = connection.get_data_frame_orders('select id_order,send_value from orders')
    df_d = connection.get_data_frame_orders('select id_order,price_unit,quantity_d_o,discount_d_o from details_orders')
    df_res = pd.merge(df_o, df_d, how='left', on='id_order')
    df_res['Total'] = df_res['send_value'] + ((df_res['price_unit']*df_res['quantity_d_o']) +
                      (df_res['price_unit']*df_res['quantity_d_o'])*df_res['discount_d_o'])
    df_res['Rank'] = df_res['Total'].rank(method='max', ascending=False)
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.rename(columns={'quantity_d_o':'Cantidad_Productos','id_order':'Pedido','send_value':'Valor_Envio'})
    df_res = df_res.rename(columns={'price_unit':'Precio_Unidad','discount_d_o':'Descuento'})
    return indent_json(df_res.head(10).to_json(orient = "table"))

"""
Top ordenes menos costosas
Return: return datatable in json
"""
def get_fifth_query():
    df_o = connection.get_data_frame_orders('select id_order,send_value from orders')
    df_d = connection.get_data_frame_orders('select id_order,price_unit,quantity_d_o,discount_d_o from details_orders')
    df_res = pd.merge(df_o, df_d, how='left', on='id_order')
    df_res['Total'] = df_res['send_value'] + ((df_res['price_unit']*df_res['quantity_d_o']) +
                      (df_res['price_unit']*df_res['quantity_d_o'])*df_res['discount_d_o'])
    df_res['Rank'] = df_res['Total'].rank(method='max')
    df_res = df_res.sort_values(by=['Rank'])
    df_res = df_res.rename(columns={'quantity_d_o':'Cantidad_Productos','id_order':'Pedido','send_value':'Valor_Envio'})
    df_res = df_res.rename(columns={'price_unit':'Precio_Unidad','discount_d_o':'Descuento'})
    return indent_json(df_res.head(10).to_json(orient = "table"))

"""
Cantidad de productos por proveedor (sin contar en stock)
Return: return datatable in json
"""
def get_sixth_query():
    df_p = connection.get_data_frame_orders('select * from products')
    df_s = connection.get_data_frame_orders('select * from suppliers')
    df_res = pd.merge(df_p,df_s, how='left', on='id_supplier')
    df_res = df_res.filter(items=['company_name', 'id_product']).groupby(['company_name']).sum()
    df_res = df_res.rename(columns={'id_product':'Cantidad_Productos'})
    df_res.index.names = ['Proveedor']
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de productos por proveedor (contando en stock)
Return: return datatable in json
"""
def get_seventh_query():
    df_p = connection.get_data_frame_orders('select * from products')
    df_s = connection.get_data_frame_orders('select * from suppliers')
    df_res = pd.merge(df_p,df_s, how='left', on='id_supplier')
    df_res = df_res.filter(items=['company_name', 'units_in_stock']).groupby(['company_name']).sum()
    df_res = df_res.rename(columns={'units_in_stock':'Cantidad_Productos'})
    df_res.index.names = ['Proveedor']
    return indent_json(df_res.to_json(orient = "table"))

"""
Productos vencidos por mes en el año 2022
Return: return datatable in json
"""
def get_eighth_query():
    df_p = connection.get_data_frame_orders('select * from products')
    df_p['exp_month'] = df_p['expiration_date'].dt.month
    df_res = df_p.filter(items=['product_name', 'exp_month'])
    df_res = pd.pivot_table(df_p, values=('product_name'), columns=['exp_month'], aggfunc="count")
    df_res = rename(df_res)
    return indent_json(df_res.to_json(orient = "table"))

"""
Precio total de las ordenes realizadas por compañia de envios
Return: return datatable in json
"""
def get_ninth_query():
    df_o = connection.get_data_frame_orders('select * from orders')
    df_s = connection.get_data_frame_orders('select * from shipping_company')
    df_join = pd.merge(df_o,df_s, how='left', on='id_shipping_company')
    df_res = df_join.filter(items=['shipping_company_name', 'send_value']).groupby(['shipping_company_name']).sum()
    df_res = df_res.rename(columns={'send_value':'Precio_Total'})
    df_res.index.names = ['Compania_Envios']
    return indent_json(df_res.to_json(orient = "table"))

"""
Cantidad de ordenes realizadas por compañia de envios por mes
Return: return datatable in json
"""
def get_tenth_query():
    df_o = connection.get_data_frame_orders('select * from orders')
    df_s = connection.get_data_frame_orders('select * from shipping_company')
    df_res = pd.merge(df_o,df_s, how='left', on='id_shipping_company')
    df_res['delivery_year'] = df_res['delivery_date'].dt.year
    df_res['delivery_month'] = df_res['delivery_date'].dt.month
    df_res = pd.pivot_table(df_res, values=('id_order'), index=['delivery_year','shipping_company_name'], columns=['delivery_month'], aggfunc="count")
    df_res = rename(df_res)
    df_res.index.names = ['Anio','Compania_Envios']
    return indent_json(df_res.to_json(orient = "table"))

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