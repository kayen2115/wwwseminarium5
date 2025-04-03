from flask import Blueprint, render_template, request, jsonify
from app.models import User
from datetime import datetime

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET', 'POST'])
def user_form():
    entries = []
    username = None
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user:
            entries = user.entries  # Lista PeakEntry
    return render_template('user_peaks.html', username=username, entries=entries, year=datetime.now().year)

# Prosty endpoint API (JSON)
# Ta dekorowana funkcja obsługuje zapytania HTTP kierowane pod adres:
#    /api/user/<username>/entries
@user_bp.route('/api/user/<username>/entries')
def user_entries_api(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return jsonify({"error": "Użytkownik nie istnieje"}), 404
    result = [{
        "peak": entry.peak.name,
        "date": entry.date.isoformat(),
        "notes": entry.notes
    } for entry in user.entries]
    return jsonify(result)
