# batch_twillo
A simple python script to batch sms using ~~twillo~~ Twilio.
------------------------------------------------------------

### Setup

```
pip install twilio
```

+ Make sure to check that the database you connect to has a table **contacts** with two fields **Contact** and **Number**.
+ Twilio requires the number to be in the 10 digit format, eg **7188880000**. The script adds the leading +1, and strips non-numeric characters. 
+ Lastly make sure to set your three credentials in the script itself. 

----------------------------------------------------------

### Usage

Simply

```
python batch_twillo.py
```

to send your message to everyone in the database. 