from flask import Flask,request,render_template
import json



    #check database

def chechkdb():
    file = open("intls/DB.json")
    global db
    db = json.load(file)

    #writedatabase

def writedb(user,passw,email,phone):
    chechkdb()
    x = {"name" : user,"email" :email,"num" : phone,"pass" : passw}
    temp  = db["clint"]
    temp.append(x)
    with open("intls/DB.json","w") as f:
       json.dump(db,f,indent=4)

    #flask app


app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/login')
def login(username,passw):
     pass

@app.route('/sinup')
def sinup(user,pasw,email,phone):
    pass




#
if __name__ == '__main__':
     app.run(debug=True)

