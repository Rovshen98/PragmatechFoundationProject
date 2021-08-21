from flask import Flask,render_template,redirect, url_for,request


app = Flask(__name__)

data=[]

@app.route("/hello/<name>")
def func(name):
    return render_template("index.html", name=name)

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        username=request.form['name']
        return redirect(url_for("func", name=username))
    else:
        return render_template("app.html")
    

    

if __name__=="__main__":
    app.run(debug=True)

