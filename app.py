from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/input', methods=['POST'])
def receive_input():
    data = request.get_json()

    # Check if data is received
    if not data:
        return jsonify({"error": "No input provided"}), 400

    # Example: extract fields like 'name' and 'age'
    name = data.get('name')
    age = data.get('age')

    if not name or not age:
        return jsonify({"error": "Missing 'name' or 'age' in request"}), 400

    response = {
        "message": "Data received successfully",
        "name": name,
        "age": age
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
