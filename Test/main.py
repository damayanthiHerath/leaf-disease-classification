from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
CORS(app, origins='http://localhost:8100')


@app.route('/')
def hello():
    return 'This is the Server Used for Testing'


@app.route('/api/endpoint', methods=['POST'])
def handle_post_request():
    data = request.json
    return {'message': 'Success'}


if __name__ == '__main__':
    app.run(debug=True)
