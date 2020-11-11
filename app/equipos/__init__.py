from flask import Blueprint

equipos_bp = Blueprint('equipos', __name__, template_folder='templates')

from . import routes
