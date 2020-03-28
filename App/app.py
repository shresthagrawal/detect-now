import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import time

app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def fn_landing():
	return render_template('landing.html')


@app.route('/sample')
def fn_home():
	return render_template('index.html')

@app.route('/thanks')
def fn_thanks():
	return render_template('thanks.html')

@app.route('/upload', methods=['GET', 'POST'])
def fn_upload():
	if request.method == 'POST':
		age = request.form.get("age",'na')
		gender = request.form.get("gender",'na')
		country = request.form.get("country",'na')
		temperature = request.form.get("temperature",'na')
		corona_test = request.form.get("corona_test",'na')
		if 'audio_data' not in request.files:
			flash('No file part')
			return '400'
		
		file = request.files['audio_data']
		ts = int(time.time())

		filename = country +'_'+corona_test + '_' + temperature + '_' +gender + '_' +age + '_' + str(ts) + '.mp3'
		file.save(os.path.join('upload', filename))

		print(file.filename)

	return '200'

if __name__ == '__main__':
	  app.run( port=8081, debug=True)