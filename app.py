from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask API via Jenkins!'

@app.route('/status')
def status():
    return jsonify({
        'status': 'running',
        'message': 'Flask API is up and running via Jenkins!'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
