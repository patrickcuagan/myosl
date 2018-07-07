from flask import Flask, request, render_template, url_for, redirect, make_response
import io
import csv
import os
import pandas as pd
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
		df = pd.read_json(f)
		df = df.to_csv
		print(df)
		# df = pd.read_csv(f)

		# print(df) 
		return 'success'
	else:
		return 'fail'

	return 'fail'

if __name__ == "__main__":
    app.run(debug=True)