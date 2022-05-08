from flask import Flask 

app = Flask(__name__)

@app.route("/")  # decorator denir bu satıra("")tırnakiçindeyazılır.
def hello():
    return "Hello World from Flask"
    
@app.route('/second')
def second():
    return 'Allahım her zaman bizlere güzellikleri nasip et'

@app.route('/second/third/subthird')
def third():
    return 'this is the subpage of third page'

@app.route('/forth/<string:id>')  # <buaradaboşlukolmasın>, int:id yada string:id olur bu araya yada boş koyabiliriz şöyleki; <id> şeklinde.
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True, port=2000)
    
    
    