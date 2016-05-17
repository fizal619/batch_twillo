import os

from werkzeug import secure_filename
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
	print('rendered index')
	return render_template('index.html')

@app.route('/send', methods = ['POST'])
def upload_file():
	phone_numbers = []
	if request.method == 'POST':
		f = request.files['file']
		print('file uploaded successfully')

		for line in f:
			phone_numbers.append(line)

		for num in phone_numbers:
			print(num)

		print('phone numbers loaded')
	
	return render_template('index.html')

if __name__ == '__main__':
	app.run()