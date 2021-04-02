from flask import Flask,request,render_template,url_for,session


app = Flask(__name__)


@app.route("/login/")
@app.route("/signin/")
@app.route('/')
def index():
    return render_template("signup.html")




# @app.route("/signup/")
# @app.route("/register")
# def signup():
#     return render_template("/signup.html")


session.clear()

if __name__ == '__main__':
    app.run(debug=True)
