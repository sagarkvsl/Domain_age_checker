from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        domain = request.form['domain']
        api_url = f'https://www.whatsmydns.net/api/domain?q={domain}'
        response = requests.get(api_url)
        result_data = response.json()
        return render_template('response.html', result=result_data)

if __name__ == '__main__':
    app.run(debug=True)
