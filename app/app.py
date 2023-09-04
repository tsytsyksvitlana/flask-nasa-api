from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

r = requests.get(
    'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/latest_photos?api_key=DEMO_KEY')
json_data = json.loads(r.text)


@app.route('/')
def hello_world():
    return render_template('index.html', photos=json_data['latest_photos'])


if __name__ == '__main__':
    app.run(debug=True)
