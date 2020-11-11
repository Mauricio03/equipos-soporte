from flask import Blueprint

login_bp = Blueprint('loginbp', __name__, template_folder='templates')

from . import routes
