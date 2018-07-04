from flask import Flask, request, render_template, url_for, redirect, make_response
import io
import csv
import pandas as pd
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)


@app.route('/')
def home():
    return render_template('index.html')

def transform(text_file_contents):
    return text_file_contents.replace("=", ",")

@app.route('/transform/<path:file_path>', methods=["GET", "POST"])
def transform_view(file_path):
    # f = request.files['data_file']
    # if not f:
    #     return "No file"

    # df = pd.read_csv(f)
    # print(df)

    print(file_path)
    f = open('/'+file_path)
    df = pd.read_csv(f)
    print(df)

    # return render_template('csv.html', data=df)
    return 'a'

if __name__ == "__main__":
    app.run(debug=True)