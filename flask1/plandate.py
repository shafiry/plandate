from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/_print_info')
def print_info():
    """returns the data"""
    a = request.args.get('phone')
    b = request.args.get('address')
    return jsonify(phone=a, address=b)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
