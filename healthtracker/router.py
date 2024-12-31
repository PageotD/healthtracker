from flask import render_template, jsonify, request
from .services import get_user_id, create_user, retrieve_weight_data, retrieve_sleep_data, add_weight_data, add_sleep_data, add_activity_data, retrieve_activity_data, add_calories_data, retrieve_calories_data


def register_routes(app):

    @app.route('/index')
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
        return jsonify(weight_data)

    @app.route('/weight/<user_id>', methods=['POST'])
    def post_weight(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        date = data['measurement_datetime']
        weight_value = data['weight_value']
        add_weight_data(user_id, date, weight_value)
        return jsonify({"message": f"Post weight data for {user_id}", "data": data})

    @app.route('/calories/<user_id>', methods=['GET'])
    def get_calories(user_id):
        """Get the weight data for the last 90 days."""
        calories_data = retrieve_calories_data(user_id)
        return jsonify(calories_data)

    @app.route('/calories/<user_id>', methods=['POST'])
    def post_calories(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        date = data['measurement_datetime']
        calories_value = data['calories_value']
        add_calories_data(user_id, date, calories_value)
        return jsonify({"message": f"Post calories data for {user_id}", "data": data})

    @app.route('/sleep/<user_id>', methods=['GET'])
    def get_sleep(user_id):
        sleep_data = retrieve_sleep_data(user_id)
        return jsonify(sleep_data)

    @app.route('/sleep/<user_id>', methods=['POST'])
    def post_sleep(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        print(data)
        add_sleep_data(user_id, data['start_datetime'], data['end_datetime'])
        return jsonify({"message": f"Post sleep data for {user_id}", "data": data})

    @app.route('/activity/<user_id>', methods=['GET'])
    def get_activity(user_id):
        """Serve the JSON data to be used by Chart.js."""
        activity_data = retrieve_activity_data(user_id)
        return jsonify(activity_data)

    @app.route('/activity/<user_id>', methods=['POST'])
    def post_activity(user_id):
        """Serve the JSON data to be used by Chart.js."""
        data = request.json
        print(data)
        add_activity_data(user_id, data['start_datetime'], data['end_datetime'])
        return jsonify({"message": f"Post activity data for {user_id}", "data": data})
