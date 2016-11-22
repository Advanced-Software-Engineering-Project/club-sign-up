#!/usr/bin/env python2.7
"""
To run locally
    python server.py
Go to http://localhost:5000 in your browser
"""

import json
import os
import time
from flask import Flask, Response, request, g
from sqlalchemy import create_engine, text, exc

# Flask
app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))

#
# Connect PostgreSQL Database
#
DATABASEURI = "postgresql://dbpeng:dbpass@104.196.133.79/testdb"
#
# This line creates a database engine that knows how to connect to the URI above
#
engine = create_engine(DATABASEURI)
#
# START SETUP CODE
#
# engine.execute("""DROP TABLE IF EXISTS test;""")
engine.execute("""CREATE TABLE IF NOT EXISTS test (
  id bigint,
  name text,
  year text,
  school text,
  text text
);""")
#
# END SETUP CODE
#


@app.before_request
def before_request():
    """
    This function is run at the beginning of every web request
    (every time you enter an address in the web browser).
    We use it to setup a database connection that can be used throughout the request
    The variable g is globally accessible
    """
    try:
        g.conn = engine.connect()
    except:
        print "uh oh, problem connecting to database"
        g.conn = None

@app.teardown_request
def teardown_request(exception):
    """
    At the end of the web request, this makes sure to close the database connection.
    If you don't the database could run out of memory!
    """
    if g.conn != None:
        g.conn.close()

@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    """AUTOMATIC GET & AWAIT POST"""
    cur = g.conn.execute("""SELECT * FROM test""")
    comments = [dict(zip(row.keys(), row)) for row in cur]
    print "GET --> SELECT", comments
    cur.close()

#    with open('comments.json', 'r') as f:
#        comments = json.loads(f.read())

    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        comments.append(new_comment)

#        with open('comments.json', 'w') as f:
#            f.write(json.dumps(comments, indent=4, separators=(',', ': ')))

        # Insert Data into Database
        cmd = """INSERT INTO test VALUES (:id, :name, :year, :school, :text);"""
        print "POST --> INSERT:", new_comment
        trans = g.conn.begin()
        try:
            g.conn.execute(text(cmd), new_comment)
            trans.commit()  # transaction is not committed yet
        except exc.IntegrityError:
            trans.rollback() # this rolls back the transaction unconditionally


    return Response(
        json.dumps(comments),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), debug=True)
