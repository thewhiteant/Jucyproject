from flask import Flask,request,render_template,url_for



app = Flask(__name__)
@app.route('/')
def index():
    return render_template("/login/login.html")




if __name__ == '__main__':
     app.run()
# def chechkdb():
#     file = open("intls/DB.json")
#     global db
#     db = json.load(file)

#     #writedatabase

#json db writter

# def writedb(user,passw,email,phone):
#     chechkdb()
#     x = {"name" : user,"email" :email,"num" : phone,"pass" : passw}
#     temp  = db["clint"]
#     temp.append(x)
#     with open("intls/DB.json","w") as f:
#        json.dump(db,f,indent=4)
