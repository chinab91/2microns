""" endpoints that handles the initiation of the splash page """
from flask import jsonify, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
from app.org import mod
from app.models import Attendee_Login
from app import db
import time


@mod.route('/twilio/send', methods=['GET'])
def send_sms():
    account_sid = "AC27506cddc4b2cb5d87d4f1cd15e79862"
    auth_token  = "f48f9c199d05c594b9b75630d17a86aa"
    client = TwilioRestClient(account_sid, auth_token)
    print 'L1'
    message = client.messages.create(to="+6586661384",
                                     from_="+14803606548",
                                     body="Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")
    time.sleep(5)
    val = db.session.query(Attendee_Login).first()
    if val.count == 0:
        return '1'
    else:
        print 'L2'
        message = client.messages.create(to="+6586661384",
                                     from_="+14803606548",
                                     body="Reminder 1: Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")

        time.sleep(5)
        val = db.session.query(Attendee_Login).first()
        if val.count == 0:
            return '1'
        else:
            print 'L3'
            message = client.messages.create(to="+6586661384",
                                     from_="+14803606548",
                                     body="Reminder 2: Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")

            time.sleep(5)
            val = db.session.query(Attendee_Login).first()
            if val.count == 0:
                return '1'
            else:
                account_sid = "AC27506cddc4b2cb5d87d4f1cd15e79862"
                auth_token  = "f48f9c199d05c594b9b75630d17a86aa"
                client = TwilioRestClient(account_sid, auth_token)
                
                print 'final loop'
                message = client.messages.create(to="+6586661384",
                                                 from_="+14803606548",
                                                 body="An Uber has been sent for Shan. He will be arriving at his home in roughly 45 minutes.")
                return '1'


@mod.route("/twilio/reply", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
    from_number = '+6586661384'
    message = request.form['Body']
    print 'message is '
    print message

    val = db.session.query(Attendee_Login).first()
    val.count = 0
    db.session.commit()

    if (message == 'Y'):
        resp = twilio.twiml.Response()
        time.sleep(3)
        resp.message("An Uber has been sent for Shan. He will be arriving at his home in roughly 25 minutes.")
        return str(resp)
    return '1'

    #https://um.jublia.com/uber/redirect