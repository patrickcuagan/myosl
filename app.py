from flask import Flask, request, render_template, url_for, redirect, make_response
import io
import csv
import os
import pandas as pd
import json
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods= ['GET', 'POST'])
def upload_file():
	if request.method == 'POST':
		# f = request.files['files']
		f = request.data
		print(f)
		print(type(f))

		print('test')
		print(f.decode("utf-8"))

		decoded_f = f.decode("utf-8")
		
		jsonfile = json.loads(decoded_f)
		
		
		df = pd.DataFrame(data = jsonfile)

		print(df)
		# df = pd.read_csv(f)

		# print(df) 
		return 'success'
	else:
		return 'fail'

	return 'fail'

if __name__ == "__main__":
    app.run(debug=True)