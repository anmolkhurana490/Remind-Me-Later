from flask import Flask, request, jsonify
from datetime import datetime
from models import init_db, save_reminder, get_reminders

app = Flask(__name__)

@app.route('/api/reminder', methods=['GET', 'POST'])
def reminder():
    if request.method == 'GET':
        reminders = get_reminders()
        return jsonify(reminders)

    data = request.get_json()

    date = data.get('date')
    time = data.get('time')
    message = data.get('message')
    reminder_type = data.get('reminder_type')

    # Validation
    if not all([date, time, message, reminder_type]):
        return jsonify({'error': 'Missing required fields'}), 400

    if reminder_type not in ['sms', 'email']:
        return jsonify({'error': 'Invalid reminder type'}), 400

    try:
        # Optional: validate date and time format
        date = datetime.strptime(date, "%Y-%m-%d").date()
        time = datetime.strptime(time, "%H:%M").time()
        dateTime = datetime.combine(date, time)

        save_reminder(dateTime, message, reminder_type)
        return jsonify({'message': 'Reminder saved successfully'}), 201
    except ValueError:
        return jsonify({'error': 'Invalid date or time format'}), 400


if __name__ == '__main__':
    init_db()
    app.run(debug=True)