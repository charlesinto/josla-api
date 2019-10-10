from flask import Flask, jsonify
import json

app = Flask(__name__)

userData = {}

with open('jobs.json', 'r') as file:
    userData = json.load(file)

@app.route('/')
def Home():
    response = app.response_class(
        response=json.dumps({'message':'welcome to josla api'}),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/jobs')
def home():
    response = app.response_class(
        response=json.dumps(userData),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == "__main__":
    app.run(debug=True)