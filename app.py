from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors



app = Flask(__name__)



#localhost
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'jucy'



mysql = MySQL(app)




@app.route('/',methods=['POST','GET'])
def index():
    msg = ""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM table WHERE username = %s AND password = MD5(%s)', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return 'Logged in successfully!'
        else:
            msg = 'Incorrect username/password!'
        

    return render_template("login.html",msg=msg)



@app.route("/signup",methods=['POST','GET'])
def signup():



    msg =""
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        usere = request.form['username']
        passw = request.form['password']
        age = request.form['age']
        emil = request.form['email']
        cursor1 = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        uposthiti = cursor1.execute('SELECT * FROM table WHERE username = %s', (usere,))
        if uposthiti == 1:
                msg  = "Username alrady taken"
                return render_template("/signup.html", msg=msg)

        elif uposthiti == 0:
            x = cursor1.execute("SELECT * FROM table WHERE id")
            cursor1.execute(f"INSERT INTO table(id,username,password,age,email) VALUES({x+1},?,MD5(?),?,?)", (usere, passw, age, emil, ))
            mysql.connection.commit()
            return "Registration Done!"
        else:
            return "404 error"
            

    return render_template("/signup.html",msg=msg)


@app.route("/reset")
def reset():
        return render_template("/reset.html")

if __name__ == '__main__':
    app.run()



