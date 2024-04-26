from app.controller import queries, queries_general
from flask import Blueprint, request, send_file
from flask_cors import cross_origin

from json import loads, dumps

main = Blueprint('q_blueprint',__name__)

@main.route('/descriptions', methods=['GET'])
@cross_origin()
def get_descriptions():
    if request.method == 'GET':
        return queries.get_descriptions_json()
    else:
        return '<h2>BAD REQUEST</h2>'
    

@main.route('/first', methods=['GET','POST'])
@cross_origin()
def get_first():
    res = request.args.get('filter')
    print(request)
    if request.method == 'POST':
        return indent_json(queries.get_first_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_first_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/second", methods=['GET','POST'])
@cross_origin()
def get_second():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_second_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_second_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/third", methods=['GET','POST'])
@cross_origin()
def get_third():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_third_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_third_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/fourth", methods=['GET','POST'])
@cross_origin()
def get_fourth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_fourth_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_fourth_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/fifth", methods=['GET','POST'])
@cross_origin()
def get_fifth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_fifth_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_fifth_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/sixth", methods=['GET','POST'])
@cross_origin()
def get_sixth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_sixth_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_sixth_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/seventh", methods=['GET','POST'])
@cross_origin()
def get_seventh():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_seventh_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_seventh_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/eighth", methods=['GET','POST'])
@cross_origin()
def get_eighth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_eighth_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_eighth_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/ninth", methods=['GET','POST'])
@cross_origin()
def get_ninth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_ninth_query())
    elif request.method == 'GET':
        return indent_json(queries_general.get_ninth_query())
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/tenth", methods=['GET','POST'])
@cross_origin()
def get_tenth():
    res = request.args.get('filter')
    if request.method == 'POST':
        return indent_json(queries.get_tenth_query(res))
    elif request.method == 'GET':
        return indent_json(queries_general.get_tenth_query())
    else:
        return '<h2>BAD REQUEST</h2>'
    
@main.route("/report/excel", methods=['GET','POST'])
@cross_origin()
def get_report_xlsx():
    filter = request.args.get('filter')
    query = request.args.get('query')
    if request.method == 'POST':
        queries.get_as_excel(query, filter)
        return send_file("report.xlsx", download_name='report_' + query + '.xlsx')
    elif request.method == 'GET':
        queries_general.get_as_excel(query)
        return send_file("report.xlsx", download_name='report_' + query + '.xlsx')
    else:
        return '<h2>BAD REQUEST</h2>'

@main.route("/report/csv", methods=['GET','POST'])
@cross_origin()
def get_report_csv():
    filter = request.args.get('filter')
    query = request.args.get('query')
    if request.method == 'POST':
        queries.get_as_csv(query, filter)
        return send_file("report.csv", download_name='report_' + query + '.csv')
    elif request.method == 'GET':
        queries_general.get_as_csv(query)
        return send_file("report.csv", download_name='report_' + query + '.csv')
    else:
        return '<h2>BAD REQUEST</h2>'

def indent_json(data):
    parsed = loads(return_json(data))
    r = dumps(parsed, indent=4) 
    return r

def return_json(data):
    return data.to_json(orient = "table")