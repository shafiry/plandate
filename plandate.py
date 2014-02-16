from flask import Flask, jsonify, render_template, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
import random
import os
import sendText
"""import pymongo"""

url_params = {}
url_params['term'] = 'date'
url_params['limit'] = 10
url_params['sort'] = 0

app = Flask(__name__)

""""callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+15162387865": "Lucas"
}

@app.route("/",methods=['GET','POST'])
def hello_monkey():
    #Respond and greet the caller by name.
    
    from_number = request.values.get('From', None)
    if from_numer in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
    
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)
"""

@app.route('/_print_info')
def print_info():
    """returns the data"""

    phone = request.args.get('phone_id')
    add = request.args.get('address')
    radius = request.args.get('distance')
    activityLevel = request.args.get('activity')
    if activityLevel == 3:
        url_params['category_filter'] = 'active'
    elif activityLevel == 2:
        activities = ['bars','nightlife','arts','restaurants','fashion','artsandcrafts','zoos','skatingrinks','beaches']
        url_params['category_filter'] = activities[random.randint(0,len(activities)-1)]
    else:
        activities = ['arts','restaurants','artsandcrafts','fashion']
        url_params['category_filter'] = activities[random.randint(0,len(activities)-1)]
    
    url_params['location'] = add
    url_params['radius_filter'] = radius
    """sends the text given 'phone'"""
    response = sendText.requester('api.yelp.com', '/v2/search', url_params, '0px8qDLNaYLpwVHlGeyNzQ', 'VYdp1bHYoPayFF9Mp0Q4RP328n0','RoXmcii1RiXkAoFh1uwMZpC6_5k2iVyq', '0bbsAocDgcBsua5WvOzxU6NxGUY')
    venueName = ''
    venueLocation = []
    for key, value in response["businesses"][random.randint(0,4)].iteritems():
        if key == 'name':
            venueName = value
        if key == 'location':
            for i in range(0,len(value['display_address'])):
                venueLocation.append(value['display_address'][i])
    venue = ''
    account_sid = "ACfe656ed49f19a12b8440cb191158f0c9"
    auth_token = "8d29d5cc81e4062e1521237983c39b21"
    client = TwilioRestClient(account_sid, auth_token)    
    message = client.messages.create(to=phone, from_="+15162724635",body="Welcome to PlanDate. You should go to:\n" + venueName +"\n"+ "\n".join(venueLocation))

    return jsonify(result = phone)


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
