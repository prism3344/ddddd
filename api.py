from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # To pozwoli Twojemu JS wysłać dane z innej domeny!
dane = []
@app.route('/leak', methods=['POST'])
def leak():
    data = request.json
    dane.append(data)
    return jsonify({"status": "ok"}), 200


@app.route('/leak', methods=['GET'])
def l():
    return jsonify(dane)


if __name__ == '__main__':
    app.run(port=8000)