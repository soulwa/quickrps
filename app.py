import os
import random
from flask import Flask, render_template, request, redirect, flash
from quickrps import quick_rps, TIE, USER_WIN, CPU_WIN, rps_enum_to_str

app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "GET":
		return render_template("index.html")

	if request.method == "POST":
		
		user_choice = int(request.form["user_choice"])
		cpu_in = random.randint(0, 2)
		result = quick_rps(user_choice, cpu_in)
		reveal = "computer chose {}".format(rps_enum_to_str[cpu_in])

		if result == TIE:
			flash('tie! ' + reveal)
		elif result == CPU_WIN:
			flash('you lost... ' + reveal)
		elif result == USER_WIN:
			flash('you won! ' + reveal)

		return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
