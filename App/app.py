import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from region_classification import detect
from pyAudioAnalysis import audioTrainTest as aT
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
		weight = request.form.get("weight",'na')
		height = request.form.get("height",'na')

		lungs = request.form.get("lungs",'na')
		if 'audio_data' not in request.files:
			flash('No file part')
			return '400'
		
		file = request.files['audio_data']
		ts = int(time.time())

		filename = country +'_'+corona_test + '_' + temperature +'_' +lungs +'_' + height + '_' + weight + '_' +gender + '_' +age + '_' + str(ts) + '.wav'
		if corona_test == 'Healthy':
			file.save(os.path.join('data/uploads/not_sick', filename))
		else:
			file.save(os.path.join('data/uploads/sick', filename))

		print(file.filename)

	return '200'

def classify(fileloc, location):
	_, res, label = aT.file_classification(fileloc, "model/model", "randomforest")
	return (0.2 * detect(location)) + (0.8 * res[1])


if __name__ == '__main__':
	  app.run( port=8081, debug=True)
	  # Test Call
	  # print(classify('data/cough_validate/not_sick/audioset__-fsiDpnxeE_225_230.wav', 'Australia'))
