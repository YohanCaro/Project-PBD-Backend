from flask import Flask
from flask_cors import CORS, cross_origin

from .views import RoutesRH, RoutesOrders, RoutesGe, RoutesQueries

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

def init_app():

    app.register_blueprint(RoutesRH.main, url_prefix = '/data/rh')

    app.register_blueprint(RoutesOrders.main, url_prefix = '/data/orders')

    app.register_blueprint(RoutesGe.main, url_prefix = '/data/gesemp')

    app.register_blueprint(RoutesQueries.main, url_prefix = '/query')

    return app

