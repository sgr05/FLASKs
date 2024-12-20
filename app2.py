from flask import Flask,render_template,request
app= Flask(__name__)
@app.route("/")
def my_form():
    return render_template("hello.html")
@app.route("/",methods=["POST"])
def my_form_post():
    text=request.form["text"]
    return f"<h1>{text}</h1>"
if __name__=="__main__":
    app.run(debug=True)