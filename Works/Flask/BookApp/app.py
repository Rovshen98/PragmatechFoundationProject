from flask import Flask,render_template,request,redirect
data=[]

app=Flask(__name__)

id=1

@app.route("/admin")
def adminpanel():
    return render_template("index.html")

@app.route("/create_book", methods=["GET","POST"])
def createbook():
    if request.method=="POST":
        global id
        ad=request.form["ad"]
        yazici=request.form["yazici"]
        il=request.form["il"]
        say=request.form["say"]
        text=request.form["text"]
         
        book={
            "id":id,
            "ad":ad,
            "yazici":yazici,
            "il":il,
            "say":say,
            "text":text
        }
        data.append(book)
        id+=1
        return redirect("/show_books")
    return render_template("addbook.html")

@app.route("/show_books")
def showbook():
    book = data
    return render_template("showbook.html", book=book)

@app.route("/single_book/<int:id>")
def singlebook(id):
    book_single = {}
    for book in data:     
        if id==book["id"]:
            book_single=book
        
    return render_template("single.html",book_single=book_single)
        
@app.route("/admin/books")
def adminbook():
    book=data
    return render_template("admin.book.html",book=book) 

@app.route("/admin/delete/<int:id>") 
def delete(id):
    
    for book in data:     
        if id==book["id"]:
            data.remove(book)
    return redirect("/admin/books")
    
@app.route("/admin/update/<int:id>") 
def update(id):
    book=data 
    for book in data:
        if id==book["id"]:
            return render_template ("update.html",book=book)

if __name__=="__main__":
    app.run(debug=True)

