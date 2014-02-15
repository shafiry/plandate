from flask import Flask, jsonify, render_template, request
from twilio.rest import TwilioRestClient
app = Flask(__name__)


@app.route('/_print_info')
def print_info():
    """returns the data"""
    a = request.args.get('phone')
    b = request.args.get('address')
    print a
    """sends the text given 'phone'"""
    account_sid = "ACfe656ed49f19a12b8440cb191158f0c9"
    auth_token = "8d29d5cc81e4062e1521237983c39b21"
    client = TwilioRestClient(account_sid, auth_token)    
    message = client.messages.create(to=a, from_="+15162724635",body="Welcome to PlanDate! Creating your ideal date now. Please wait for further instructions..")

    return jsonify(phone=a, address=b)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()