import os
import sqlite3
from twilio.rest import TwilioRestClient

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

# Replace the following with your LIVE keys from here
# https://www.twilio.com/user/account/settings
account = "Axxxxxxxxxxxxxxxxxxxx"
token = "0xxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account, token)

# Edit your message here of course
Message = ', just a reminder to check out the scholarship program from Make School I emailed you about. The deadline is nearing. -Saeed Jabbar'

for row in cursor.execute('SELECT * FROM contacts'):
	Name, Phone = row
	# You can find your 'from_' parameter in your twilio dash at the following link
	# https://www.twilio.com/user/account/phone-numbers/incoming
	message = client.messages.create(to=Phone, from_="+1xxxxxxxxxx", body= Name + Message)
