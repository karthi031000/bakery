from flask import Flask, render_template, url_for

app = Flask(__name__)


desc = [['Chocolate Cake','Cup Cake','Strawberry Cake'],['Chocolate Cookies','Ordinary','Strawberry'],['Strawberry','Chocolate','Blackberry']]
price = [['500/Kg','25/piece','550/Kg'],['100/packet','75/packet','150/packet'],['250','275','300']]
product = ["cake","cookie","dessert"]
@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html",products = product,desc = desc,price = price)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/signup")
def sign():
    return render_template("signup.html")


@app.route("/login")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
