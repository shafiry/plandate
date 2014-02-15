import json
import oauth2
import optparse
import urllib
import urllib2

url_params = {}
url_params['term'] = 'bars'
url_params['location'] = 'philadelphia'
url_params['limit'] = 3
url_params['radius_filter'] = 15000
url_params['category_filter'] = 'bars'
url_params['sort'] = 0

def request(host, path, url_params, consumer_key, consumer_secret, token, token_secret):
  """Returns response for API request."""
  # Unsigned URL                                                                                                                                                                     
  encoded_params = ''
  if url_params:
    encoded_params = urllib.urlencode(url_params)
  url = 'http://%s%s?%s' % (host, path, encoded_params)
  print 'URL: %s' % (url,)

  # Sign the URL                                                                                                                                                                     
  consumer = oauth2.Consumer(consumer_key, consumer_secret)
  oauth_request = oauth2.Request('GET', url, {})
  oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                        'oauth_timestamp': oauth2.generate_timestamp(),
                        'oauth_token': token,
                        'oauth_consumer_key': consumer_key})

  token = oauth2.Token(token, token_secret)
  oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
  signed_url = oauth_request.to_url()
  print 'Signed URL: %s\n' % (signed_url,)

  # Connect                                                                                                                                                                          
  try:
    conn = urllib2.urlopen(signed_url, None)
    try:
      response = json.loads(conn.read())
    finally:
      conn.close()
  except urllib2.HTTPError, error:
    response = json.loads(error.read())

  return response

response = request('api.yelp.com', '/v2/search', url_params, '0px8qDLNaYLpwVHlGeyNzQ', 'VYdp1bHYoPayFF9Mp0Q4RP328n0', 'RoXmcii1RiXkAoFh1uwMZpC6_5k2iVyq', '0bbsAocDgcBsua5WvOzxU6NxGUY')
sms_message = ''
for key,value in response["businesses"][1].iteritems():
  if key == 'name':
    sms_message = value

from twilio.rest import TwilioRestClient

account_sid = "ACfe656ed49f19a12b8440cb191158f0c9"
auth_token = "8d29d5cc81e4062e1521237983c39b21"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+15162387865", from_="+15162724635",body=sms_message)

