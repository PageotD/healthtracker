from flask import render_template, jsonify, request

def register_routes(app):
    @app.route('/')
    def index():
        """Render the HTML page that will show the charts."""
        return render_template('index.html')

    @app.route('/user/<user_id>', methods=['GET'])
    def get_user(user_id):
        """Serve the JSON data to be used by Chart.js."""
        return jsonify({"message": f"Get user data for {user_id}"})

    @app.route('/weight/<user_id>', methods=['GET'])
    def get_weight(user_id):
        """Serve the JSON data to be used by Chart.js."""
        return jsonify({"message": f"Get weight data for {user_id}"})

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
