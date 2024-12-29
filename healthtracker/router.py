from flask import render_template, jsonify, request
import sqlite3
import uuid
from .services import get_user_id, create_user, retrieve_weight_data

def register_routes(app):

    @app.route('/')
    def index():
        """Render the HTML page that will show the charts."""
        return render_template('index.html')

    @app.route('/user/<user_name>', methods=['GET'])
    def get_user(user_name):
        """Get user ID."""
        user_id = get_user_id(user_name)
        return jsonify({"user_id": user_id}), 200

    @app.route('/user/<user_name>', methods=['POST'])
    def post_user(user_name):
        """Create a new user."""
        user_id = get_user_id(user_name)
        if user_id:
            return jsonify({"message": "User already exists"}), 400
        create_user(user_name)
        return jsonify({"message": "User created successfully"}), 201

    @app.route('/weight/<user_id>', methods=['GET'])
    def get_weight(user_id):
        """Get the weight data for the last 90 days."""
        weight_data = retrieve_weight_data(user_id)
        return jsonify([{"measurement_datetime": measurement_datetime, "weight_value": weight_value} for measurement_datetime, weight_value in weight_data])

    @app.route('/weight/<user_id>', methods=['POST'])
    def post_weight(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        return jsonify({"message": f"Post weight data for {user_id}", "data": data})

    @app.route('/sleep/<user_id>', methods=['GET'])
    def get_sleep(user_id):
        """Serve the JSON data to be used by Chart.js."""
        return jsonify({"message": f"Get sleep data for {user_id}"})

    @app.route('/sleep/<user_id>', methods=['POST'])
    def post_sleep(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        return jsonify({"message": f"Post sleep data for {user_id}", "data": data})

    @app.route('/activity/<user_id>', methods=['GET'])
    def get_activity(user_id):
        """Serve the JSON data to be used by Chart.js."""
        return jsonify({"message": f"Get activity data for {user_id}"})

    @app.route('/activity/<user_id>', methods=['POST'])
    def post_activity(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        return jsonify({"message": f"Post activity data for {user_id}", "data": data})
