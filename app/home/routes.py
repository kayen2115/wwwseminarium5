from flask import Blueprint, render_template
from app.models import Peak
from datetime import datetime

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def homepage():
    peaks = Peak.query.all()
    return render_template('home.html', peaks=peaks, year=datetime.now().year)
