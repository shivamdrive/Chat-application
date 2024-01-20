import imp
from urllib import request
from colorama import Cursor
from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import os

app = Flask(__name__)
picFolder = os.path.join('static','images')


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Shivanshu2211'
app.config['MYSQL_DB'] = 'whatsapp'
# app.config['UPLOAD_FOLDER'] = picFolder

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userDetails = request.form
        cur = mysql.connection.cursor()
        cur.execute("select count(*) from Chat_History")
        result = cur.fetchall()
        chat_id = result[0][0]+1

        #chat_id = userDetails["chat_id"]
        # sender_id = userDetails["sender_id"]
        # receiver_id = userDetails["receiver_id"]
        # date = userDetails["date"]
        # time = userDetails["time"]
        decription = userDetails["decription"]
        # chat_in_group = userDetails["chat_in_group"]
        # group_id = userDetails["group_id"]

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO Chat_History(chat_id,sender_id,receiver_id,date,time,decription,chat_in_group,group_id) VALUES(%s,'1','2','2001-01-20','8:00PM',%s,'No',NULL)",(chat_id,decription))
        mysql.connection.commit()
        cur.close()
        return redirect('/chat_history')

    return render_template('whatsapp.html')


@app.route('/chat_history')
def chat_history():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Chat_History")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('chat_history.html', userDetails=userDetails)

@app.route('/user')
def user():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM User")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('user.html', userDetails=userDetails)


@app.route('/group')
def group():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM G_roup")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('group.html', userDetails=userDetails)


@app.route('/chat')
def chat():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Chat")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('chat.html', userDetails=userDetails)


@app.route('/call')
def call():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM C_all")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('call.html', userDetails=userDetails)


@app.route('/call_history')
def call_history():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Call_History")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('call_history.html', userDetails=userDetails)


@app.route('/status')
def status():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM S_tatus")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('status.html', userDetails=userDetails)


@app.route('/status_group')
def status_group():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Status_Group")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('status_group.html', userDetails=userDetails)


@app.route('/media')
def media():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM Media")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('media.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run(debug=True)