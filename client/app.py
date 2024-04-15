from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_GATEWAY_URL = "http://localhost:5000/api/person"  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        response = requests.post(API_GATEWAY_URL, json={'name': name, 'role': role})
        return jsonify(response.json())
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000, debug=True)
