from flask import Flask, request
from flask import jsonify

app = Flask(__name__)



@app.route("/")
def inicial():
    return jsonify("hola mundo")




if __name__ == "__main__":
    app.run(debug=True)