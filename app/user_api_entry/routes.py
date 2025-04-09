from flask import Blueprint, render_template, request, jsonify
from .. import db
from ..models import User, Peak, PeakEntry
from datetime import datetime

def add_entry(username, peak, date, notes):
    try :
        # Convert the date string to a datetime object
        date = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        return 5
    # Find the user and peak in the database
    user = User.query.filter_by(username=username).first()
    peak = Peak.query.filter_by(name=peak).first()

    if user and peak:
        # Create a new entry
        new_entry = PeakEntry(user_id=user.id, peak_id=peak.id, date=date, notes=notes)
        db.session.add(new_entry)
        db.session.commit()
        return 1  # Return a success response
    elif not user:
        return 2
    elif not peak:
        return 3 # Return an error response
    else:
        return 4 # Return an error response
    # If the user or peak does not exist, return an error response

user_api_entry_bp = Blueprint('user_api_entry', __name__)

@user_api_entry_bp.route('/users/api/entry', methods=['GET', 'POST'])
def user_api_entry_form():
    if request.method == 'POST':
        
        if not request.is_json:
            return jsonify({"error": "Invalid content type"}), 400
        # Extract data from the request
        data = request.get_json()
        username = data.get('username')
        peak = data.get('peak')
        date = data.get('date')
        notes = data.get('notes')

        # Call the add_entry function to add the entry to the database
        response = add_entry(username, peak, date, notes)
        if response == 1:
            return jsonify({"message": "Entry added successfully"}), 201
        elif response == 2:
            return jsonify({"error": "User not found"}), 400
        elif response == 3:
            return jsonify({"error": "Peak not found"}), 400
        elif response == 4:
            return jsonify({"error": "Failed to add entry"}), 400
        elif response == 5:
            return jsonify({"error": "Invalid date format"}), 400

      
    return render_template('user_peaks_api_entry.html')

