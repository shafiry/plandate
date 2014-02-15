from flask import Flask, jsonify, render_template, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient

import sendText
"""import pymongo"""

url_params = {}
url_params['term'] = 'movie'
url_params['limit'] = 3
url_params['category_filter'] = 'movietheaters'
url_params['sort'] = 0

app = Flask(__name__, static_url_path = "", static_folder = "static")

@app.route('/_print_info')
def print_info():
    """returns the data"""

    phone = request.args.get('phone_id')
    add = request.args.get('address')
    dist = request.args.get('distance')
    print phone
    print add
    print dist
    url_params['location'] = add
    url_params['radius_filter'] = 10000
    """sends the text given 'phone'"""
    response = sendText.requester('api.yelp.com', '/v2/search', url_params, '0px8qDLNaYLpwVHlGeyNzQ', 'VYdp1bHYoPayFF9Mp0Q4RP328n0','RoXmcii1RiXkAoFh1uwMZpC6_5k2iVyq', '0bbsAocDgcBsua5WvOzxU6NxGUY')
    venue = ''
    for key, value in response["businesses"][0].iteritems():
        if key == 'name':
            venue = value
        if key == 'location':
            for i in range(0,len(value['display_address'])):
                print value['display_address'][i]
    account_sid = "ACfe656ed49f19a12b8440cb191158f0c9"
    auth_token = "8d29d5cc81e4062e1521237983c39b21"
    client = TwilioRestClient(account_sid, auth_token)    
    message = client.messages.create(to=phone, from_="+15162724635",body="Welcome to PlanDate. You should go to " + venue)

    return jsonify(result = phone)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming calls with a simple text message."""
 
    resp = twilio.twiml.Response()
    resp.message("Hello, Mobile Monkey")
    return str(resp)

if __name__ == '__main__':
    app.run()
