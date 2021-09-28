from flask import Flask
import json
from flask import request
from datetime import datetime
import psycopg2

# Create an instance of the Flask class that is the WSGI application.
# The first argument is the name of the application module or package,
# typically __name__ when using a single module.
app = Flask(__name__)

# Flask route decorators map / and /hello to the hello function.
# To add other resources, create functions that generate the page contents
# and add decorators to define the appropriate resource locators for them.

conn = psycopg2.connect(host="ec2-54-211-160-34.compute-1.amazonaws.com",database="d2dk8jrg0rkivc",user="fggzjksrvftylq",password="691b44a66cfc74d46d3a40e0faba3e00ae8cb6aafc1e3ed7a9b755de6ee5eb4c")

@app.route('/')
@app.route('/hello')
def hello():
    data="123"
    return data

@app.route('/getUsers')
def getUsers():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vw_users')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return json.dumps(results)

@app.route('/getEventDates')
def getEventDates():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_eventDates')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return json.dumps(results)

@app.route('/setEvents')
def setEvents():
    cursor = conn.cursor()
    insert_records = '''INSERT INTO tbl_events (eventDate_id,user_id)
                VALUES(?,?) '''
    cursor.execute(insert_records,request.args['eventDate_id'],request.args['user_id'])
    conn.commit()
    return 'Inserted'

@app.route('/setUsers')
def setUsers():
    cursor = conn.cursor()
    insert_records = '''INSERT INTO bt_interviews.dbo.tbl_users (Name)
                VALUES(?) '''
    cursor.execute(insert_records,request.args['name'])
    conn.commit()
    cursor.execute('SELECT Top 1 id FROM tbl_users ORDER BY entered_date DESC')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return json.dumps(results)

@app.route('/getEvents')
def getEvents():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tbl_events')
    columns = [column[0] for column in cursor.description]
    results = []
    for row in cursor.fetchall():
        results.append(dict(zip(columns, row)))
    return json.dumps(results)

@app.route('/setEventDates', methods = ['Get'])
def setEventDates():
    cursor = conn.cursor()
    insert_records = '''INSERT INTO tbl_eventDates (eventDate,eventTime)
                VALUES(?,?) '''
    cursor.execute(insert_records,datetime.strptime(request.args['eventDate'],'%d/%m/%y'),datetime.strptime(request.args['eventTime'],'%H:%M:%S'))
    conn.commit()
    return 'Inserted'

if __name__ == '__main__':
    # Run the app server on localhost:4449
    app.run('localhost', 4449)