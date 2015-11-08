from flask import Blueprint

mod = Blueprint('org', __name__)
from app.org.views import twiliov, telegramv