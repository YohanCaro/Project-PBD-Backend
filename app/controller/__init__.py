from flask import Blueprint

bp = Blueprint('main', __name__)

from app.controller import queries