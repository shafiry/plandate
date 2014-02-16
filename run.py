from flask import Flask,request,redirect
import twilio.twiml

app = Flask(__name__)

callers = {
    "+14158675309": "Curious George",
    "+14158675310": "Boots",
    "+14158675311": "Virgil",
    "+15162387865": "Lucas"
}

@app.route("/",methods=['GET','POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    
    from_number = request.values.get('From', None)
    if from_numer in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
    
    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)
    

if __name__ == "__main__":
    app.run(debug=True)
