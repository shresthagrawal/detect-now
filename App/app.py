import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from region_classification import detect
from pyAudioAnalysis import audioTrainTest as aT
import json
import time

app = Flask(__name__)
app.secret_key = 'super secret key'


@app.route('/')
def fn_landing():
	return render_template('landing.html')

@app.route('/test')
def fn_test():
	return render_template('test.html')

@app.route('/sample')
def fn_home():
	return render_template('index.html')

@app.route('/thanks')
def fn_thanks():
	return render_template('thanks.html')

@app.route('/upload', methods=['GET', 'POST'])
def fn_upload():
	upload_save(request, False)
	return '200'

@app.route('/upload_test', methods=['GET', 'POST'])
def fn_upload_test():
	path = upload_save(request, True)
	# TODO: Add function to converg age to int
	# request.form.get("age",'na')
	res = classify(
		path, 
		request.form.get("country",'na'),
		request.form.get("gender",'na'),
		24
		)
	return json.dumps({'result': res})

def upload_save(request, tmp):
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
		
		p = ''
		if tmp == True:
			p = os.path.join('data/uploads/tmp', filename)
		elif corona_test == 'Healthy':
			p = os.path.join('data/uploads/not_sick', filename)
		else:
			p = os.path.join('data/uploads/sick', filename)
		
		file.save(p)
		return p


def classify(fileloc, location, gender, age):
	_, res, label = aT.file_classification(fileloc, "model/model", "randomforest")
	print(detect(location, gender, age), res[1])
	# return (0.2 * detect(location, gender, age)) + (0.8 * res[1])
	return res[1]


if __name__ == '__main__':
	  app.run( port=8081, debug=True)
	  # Test Call
	  # print(classify('data/cough_validate/sick/audioset_-CwXrwgVffM_35_40.wav', 'Australia', 'male', 70))
