# quickrps

This is a website designed to play rock-paper-scissors against a random computer opponent. It's built using Flask and sqlite3
to maintain a database tracking global wins, losses, and ties.

To set up the database and run the website, run
```bash
$ pip install -r requirements.txt
$ python
>>> from app import init_db()
>>> init_db()
>>> quit
$ flask run
```
in your terminal.
