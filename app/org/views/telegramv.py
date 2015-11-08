from flask import jsonify, request, redirect
import twilio.twiml
from twilio.rest import TwilioRestClient
from app.org import mod
from app import db
import telegram
from app.models import Attendee_Login
import time

global bot
bot = telegram.Bot(token='154932919:AAHFXFI5yI0Y9iml7KTiLcgLRqYbwpDUj8A')

@mod.route('/telegram/hook', methods=['POST'])
def webhook_handler():
	if request.method == "POST":
		# retrieve the message in JSON and then transform it to Telegram object
		print 'here'
		val = db.session.query(Attendee_Login).first()
		val.count = 0
		db.session.commit()
		print 'complete'

		update = telegram.Update.de_json(request.get_json(force=True))

		chat_id = update.message.chat.id

		# Telegram understands UTF-8, so encode text for unicode compatibility
		text = update.message.text.encode('utf-8')

		# repeat the same message back (echo)
		if text == telegram.Emoji.THUMBS_UP_SIGN:
			msg = "Stay here boys, I'll be back with an Uber %s" % (telegram.Emoji.THUMBS_UP_SIGN)
			bot.sendMessage(chat_id=chat_id, text=msg)
			reply_markup = telegram.ReplyKeyboardHide()
	return 'ok'


@mod.route('/', methods=['GET', 'POST'])
def set_webhook():
	s = bot.setWebhook('https://um.jublia.com/telegram/hook')
	account_sid = "AC27506cddc4b2cb5d87d4f1cd15e79862"
	auth_token  = "f48f9c199d05c594b9b75630d17a86aa"
	client = TwilioRestClient(account_sid, auth_token)
	if s:
		val = db.session.query(Attendee_Login).first()
		val.count = 1 #starts with 1 everytime
		db.session.commit()
		bot.sendMessage(chat_id=str(-59647521), text="Hi @chinab91, @shannietron has crossed the 0.08 threshold of BAC.")
		custom_keyboard = [[ telegram.Emoji.THUMBS_UP_SIGN, telegram.Emoji.THUMBS_DOWN_SIGN ]]
		reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
		bot.sendMessage(chat_id=str(-59647521), text="I can help you call an Uber so he reaches home safely. Would either of you want me to do that?", reply_markup=reply_markup)
		time.sleep(5)
		print 'checking for sms'
		print 'L1'
		message = client.messages.create(to="+6586661384",
										 from_="+14803606548",
										 body="Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")
		time.sleep(3)
		val = db.session.query(Attendee_Login).first()
		if val.count == 0:
			return '1'
		else:
			print 'L2'
			message = client.messages.create(to="+6586661384",
										 from_="+14803606548",
										 body="Reminder 1: Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")

			time.sleep(3)
			val = db.session.query(Attendee_Login).first()
			if val.count == 0:
				return '1'
			else:
				print 'L3'
				message = client.messages.create(to="+6586661384",
										 from_="+14803606548",
										 body="Reminder 2: Hey Chinab, Shan is drunk at The Hub, 128 Prinsep Street, 188655 Singapore. Do you want to call for an Uber? Y or N")

				time.sleep(3)
				val = db.session.query(Attendee_Login).first()
				if val.count == 0:
					return '1'
				else:
					"""print 'final loop'
					time.sleep(5)
					message = client.messages.create(to="+6586661384",
													 from_="+14803606548",
													 body="An Uber has been sent for Shan. He will be arriving at his home in roughly 45 minutes.")"""
					return '1'

		return "webhook setup ok"
	else:
		return "webhook setup failed"


@mod.route('/telegram')
def index():
	return '.'

@mod.route('/abc')
def abc():
	