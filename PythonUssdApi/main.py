import os
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route("/ussd", methods = ['POST'])
def ussd():
    # Read the variables sent via POST from our API
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "default")

    print(text)

    if text      == '':
        # This is the first request. Note how we start the response with CON
        response  = "CON Welcome to Kiwi Insure. Please select an option below: \n"
        response += "1. New Policy or Information \n"
        response += "2. My Account \n"

    elif text    == '1':
        # Business logic for first level response
        response  = "CON Please enter your ID number and answer the call that you will receive or cancel\n"
        # response += "1. Ok \n"
        response += "2. Cancel \n"

    elif text   == '2':
        # Business logic for the second option
        response = "CON My Account.\nPlease select an option:\n"
        response += "1. Make Payment\n"
        response += "2. Account status\n"
        response += "3. Submit Claim or Log Query\n"

    elif len(text)  >= 9:
        response  = "END Thank you for choosing Kiwi Insure \n"
        make_insurance_call()

    elif text  == '1*2':
        response  = "END Transaction cancelled. See you soon. \n"

    elif text   == '2*1':
        # Business logic for the second option
        response = "CON Please note that R51.00 will be debited from your airtime balance, confirm:\n"
        response += "1. Ok\n"
        response += "2. Cancel\n"

    elif text   == '2*2':
        # Business logic for the second option
        response = "END Account status: Active\nPremium Amount: R51\nNumber of beneficiaries: 3\nRewards Balance: 1300 points"

    elif text   == '2*3':
        # Business logic for the second option
        response = "CON Please answer the claims call.\n"
        response += "1. Ok\n"
        make_insurance_call()

    elif text   == '2*2*1':
        # Business logic for the second option
        response = "END Payment successful.\n"
        response += "Account status: Active\nPremium Amount: R51\nNumber of beneficiaries: 3\nRewards Balance: 1300 points\n"

    elif text   == '2*2*2':
        # Business logic for the second option
        response = "END Payment cancelled.\n"
        
    else :
        response = "END Invalid choice"

  # Send the response back to the API
    return response

@app.route('/')
def index():
    return "<h1>Welcome to our server!</h1>"

def make_insurance_call():
    url = "http://a356-154-117-131-230.ngrok.io/dasha"
    requests.get(url=url)

if __name__ == '__main__':
    app.run(debug=True)