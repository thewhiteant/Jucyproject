from flask import Flask,request,render_template,url_for


app = Flask(__name__)

@app.route("/login")
@app.route("/signup")
@app.route('/')
def index():
    return render_template("login.html")

@app.route("/sinup")
@app.route("/register")
def signup():
    render_template("")




if __name__ == '__main__':
    app.run()

