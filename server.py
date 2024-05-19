from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)


with open('./Data/data.json') as f:
    data = json.load(f)

@app.route('/')
def index():
    latest_year = '2022'
    total_increase = sum(float(item[latest_year]) for item in data if 'Consumer Price Index item' in item)
    return render_template('index.html', total_increase=total_increase, latest_year=latest_year)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/micro')
def micro():
    food_type = request.args.get('foodType', 'All food')
    filtered_data = [item for item in data if item['Consumer Price Index item'] == food_type]
    if filtered_data:
        return render_template('micro_page.html', data=filtered_data[0])
    else:
        return render_template('micro_page.html', data={})

if __name__ == '__main__':
    app.run(debug=True)
