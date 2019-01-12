from flask import Flask,render_template

app=Flask(__name__)
app.secret_key = 'secret123'
@app.route("/")
@app.route("/home")
def home():
    return render_template("HTMLSDL.html")
if __name__ == '__main__':
    app.run(debug=True, port='80')