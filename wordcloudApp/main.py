from flask import Flask, flash, redirect, render_template, request, session, abort
import tweet2csv
import subprocess
from wordcloud import WordCloud
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello():
	tweet2csv.main('Twitter')
	text = open("output.csv").read()
	wc = WordCloud()
	wc.generate(text)
	var = "./static/images/Twitter.png"
	wc.to_file(var)
	return render_template("index.html", user_image = "../static/images/Twitter.png")

@app.route('/create',methods=['POST','GET'])
def Create():
	_name = request.form['inputName']
	if _name:
		tweet2csv.main(str(_name))
		text = open("output.csv").read()
		wc = WordCloud()
		wc.generate(text)
		var = "./static/images/" + str(_name) + ".png"
		wc.to_file(var)
		var1 = "/static/images/" + str(_name) + ".png"
		return render_template("img.html", user_image = "../"+str(var1))

if __name__ == "__main__":
	app.run()