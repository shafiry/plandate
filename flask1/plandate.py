from flask import Flask, jsonify, render_template, request
import pymongo

app = Flask(__name__)

@app.route('/_print_info')
def print_info():
    """returns the data"""
    phone = request.args.get('phone_id')
    add   = request.args.get('address')
    return jsonify(result = phone)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
