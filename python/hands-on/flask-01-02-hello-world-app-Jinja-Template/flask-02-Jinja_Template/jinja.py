from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=34, number2=45)

@app.route("/mult")
def number():
    num1 = 11  # burada num1, num2 = 5, 8 şeklinde de yazılabilir.
    num2 = 99
    return render_template("body.html", value1=num1, value2=num2, multiplation=num1*num2)



if __name__== "__main__":
    app.run(debug=True)