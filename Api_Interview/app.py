from flask import Flask
import json
from flask import request
from datetime import datetime
import random
import pyodbc as odbccon
conn = odbccon.connect('Driver={SQL Server};'
                      'Server=DESKTOP-1VDKEN9\SQLEXPRESS;'
                      'Database=bt_interviews;'
                      'Trusted_Connection=yes;')
app = Flask(__name__)


@app.route('/')
@app.route('/getUsers')
def getUsers():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_users')
    columns = [column[0] for column in cursor.description]
    columns.append("Random")
    results = []
    for row in cursor.fetchall():
        row_to_list = [elem for elem in row]
        row_to_list.append(random.randint(1,100))
        results.append(dict(zip(columns, row_to_list)))
    return json.dumps(results)

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)