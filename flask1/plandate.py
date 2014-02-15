from flask import Flask, jsonify, render_template, request
<<<<<<< HEAD

from twilio.rest import TwilioRestClient

import sendText
"""import pymongo"""

url_params = {}
url_params['term'] = 'movie'
url_params['location'] = '19123'
url_params['limit'] = 3
url_params['radius_filter'] = 15000
url_params['category_filter'] = 'movietheaters'
url_params['sort'] = 0
=======
from twilio.rest import TwilioRestClient
import json
import pymongo
>>>>>>> c1b9ea22bec53313eb91920277aee9007dceaff8

app = Flask(__name__)

@app.route('/_print_info')
def print_info():
    """returns the data"""
<<<<<<< HEAD

    phone = request.args.get('phone_id')
    add = request.args.get('address')
    print phone
    print add
    
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
=======
    phone = request.args.get('phone_id')
    add   = request.args.get('address')
    #sends the text given 'phone'
    account_sid = "ACfe656ed49f19a12b8440cb191158f0c9"
    auth_token = "8d29d5cc81e4062e1521237983c39b21"
    client = TwilioRestClient(account_sid, auth_token)    
    message = client.messages.create(to=phone, from_="+15162724635",body="Welcome to PlanDate! Creating your ideal date now. Please wait for further instructions..")

    my_dict = {"phone_id":phone, "address":add}

    return jsonify(result=my_dict)
>>>>>>> c1b9ea22bec53313eb91920277aee9007dceaff8


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
