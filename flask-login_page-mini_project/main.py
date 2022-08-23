
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/", methods = ['GET'])
def Home():
    return render_template("index.html")
@app.route("/login", methods = ['GET','POST'])
def login():
    database = {"rahul":"password","Admin":"Admin"}

    if request.method == "POST":
        
        username = request.form["uname"]
        password = request.form["upass"]
        if username in database.keys() and password in database.values():

            return render_template("login.html",html_var = username )
        else:
            return render_template("invalid.html")

if __name__ == "__main__":
    app.run(debug= True)
