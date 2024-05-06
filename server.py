from flask import Flask, jsonify, render_template, request
import json
import math

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    f = open("Data/data.json","r")
    data = json.load(f)
    f.close()
    


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
