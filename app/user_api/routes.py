from flask import Blueprint, render_template

user_api_bp = Blueprint('user_api', __name__)

@user_api_bp.route('/users/api')
def user_api_form():
    return render_template('user_peaks_api.html')