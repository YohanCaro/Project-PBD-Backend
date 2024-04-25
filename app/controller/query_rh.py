from app.db import connection
from json import loads, dumps

def indent_json(data):
    parsed = loads(data)
    r = dumps(parsed, indent=4) 
    return r

def get_all_employees():
    df_emp = connection.get_data_frame_rh('select * FROM employees')
    return indent_json(df_emp.to_json(orient = "table"))

def get_all_jobs():
    df_emp = connection.get_data_frame_rh('select * FROM jobs')
    return indent_json(df_emp.to_json(orient = "table"))

def get_all_job_histories():
    df_emp = connection.get_data_frame_rh('select * FROM job_histories')
    return indent_json(df_emp.to_json(orient = "table"))

def get_all_departments():
    df_emp = connection.get_data_frame_rh('select * FROM departments')
    return indent_json(df_emp.to_json(orient = "table"))