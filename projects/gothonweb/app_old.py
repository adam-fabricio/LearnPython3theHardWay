"""Exercise 50 - Your Firs Website."""


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = "Hello World"
    greeting = None
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()
