# This file provided by Facebook is for non-commercial testing and evaluation
# purposes only. 

# Modified by Peng on Mon Oct  3 21:57:03 2016

import json
import os
import time
import psycopg2
from flask import Flask, Response, request

# logfile
flog=open('server.log','w')

# Connect PostgreSQL Database
try:
    conn = psycopg2.connect("dbname='asehwdb' user='dbpeng' host='localhost' password='dbpass'")
except:
    flog.write("Unable to connect to the database\n")
try:
    cur = conn.cursor()
except:
    pass


# Flask
app = Flask(__name__, static_url_path='', static_folder='public')
app.add_url_rule('/', 'root', lambda: app.send_static_file('index.html'))


@app.route('/api/comments', methods=['GET', 'POST'])
def comments_handler():
    with open('comments.json', 'r') as f:
        comments = json.loads(f.read())

    if request.method == 'POST':
        new_comment = request.form.to_dict()
        new_comment['id'] = int(time.time() * 1000)
        comments.append(new_comment)

        with open('comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4, separators=(',', ': ')))
            
        # Insert Data into Database
        try:
            cur.execute(
            """INSERT INTO registered VALUES (%(id)s, %(name)s, %(text)s, %(school)s, %(year)s);""",
            new_comment)
            conn.commit()
        except:
            flog.write("Unable to insert\n")
            

    return Response(
        json.dumps(comments),
        mimetype='application/json',
        headers={
            'Cache-Control': 'no-cache',
            'Access-Control-Allow-Origin': '*'
        }
    )


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 3001)), debug=True)
