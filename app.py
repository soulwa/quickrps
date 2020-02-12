import os
import random
import sqlite3
from flask import Flask, render_template, request, redirect, flash, g
from quickrps import quick_rps, TIE, USER_WIN, CPU_WIN, rps_enum_to_str

app = Flask(__name__)

DATABASE = os.path.join(os.path.abspath('.'), "rps.db")

def get_db():
	db = getattr(g, '_database', None)
	if db is None:
		db = g._database = sqlite3.connect(DATABASE)
	db.row_factory = sqlite3.Row
	return db

@app.teardown_appcontext
def teardown_db(exception):
	db = g.pop('_database', None)
	if db is not None:
		db.close()

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('rps.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()

app.config['SECRET_KEY'] = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def index():

	if request.method == "GET":
		cur = get_db().cursor()
		cur.execute("SELECT * FROM WINS")
		wins = cur.fetchall()
		return render_template("index.html", wins=wins)

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

		db = get_db()
		db.cursor().execute("UPDATE wins SET COUNT = COUNT + 1 WHERE ID = ?", (result, ))
		db.commit()

		return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
