import os
import sqlite3
import re

from twilio.rest import TwilioRestClient

# For whatever database you'll have. Just made sure you have the appropriate data.
conn = sqlite3.connect('db.db') 
cursor = conn.cursor()

# Replace the following with your LIVE keys from here
# https://www.twilio.com/user/account/settings
account = "Axxxxxxxxxxxxxxxxxxxx"
token = "0xxxxxxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account, token)

# Edit your message here of course
Message = ', just a reminder to check out xyz'

for row in cursor.execute('SELECT * FROM contacts'): #make sure to customize for your database table.
	Name, Phone = row
	Phone = '+1' + re.sub('[^0-9]','', Phone)
	# You can find your 'from_' parameter in your twilio dash at the following link
	# https://www.twilio.com/user/account/phone-numbers/incoming
	message = client.messages.create(to=Phone, from_="+1xxxxxxxxxx", body= Name + Message)
