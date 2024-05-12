from flask import Flask, jsonify, render_template, request
import json
import math

app = Flask(__name__)

@app.route('/')
def index():
    f = open("Data/data.json","r")
    data = json.load(f)
    f.close()
    
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
