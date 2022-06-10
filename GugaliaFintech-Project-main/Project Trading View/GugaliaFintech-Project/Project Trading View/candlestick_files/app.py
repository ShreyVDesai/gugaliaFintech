from get_VIP_graph_html import get_graph
from flask import Flask, render_template, Response, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('main.html')


@app.route('/fig')
def fig():
    return jsonify(get_graph())

if __name__ == '__main__':
    app.run(debug=True, port=3000)