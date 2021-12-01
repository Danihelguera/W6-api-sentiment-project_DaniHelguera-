from flask import Flask, request
from flask import jsonify
from sqlalchemy.sql.functions import user
import config.sql_tools as sqt


app = Flask(__name__)

@app.route("/")
def inicial():
    return "HOLA MUNDO"

@app.route("/user_list")
def give_me_users():
    return jsonify(sqt.users_list())

@app.route("/product_list")
def give_me_products():
    return jsonify(sqt.products_list())

@app.route("/ratingsbyuser")
def give_me_ratings_by_user():
    user = request.form.get("user")
    return jsonify(sqt.ratings_by_user(user))

@app.route("/ratingsbyproduct")
def give_me_ratings_by_product():
    product = request.form.get("product")
    return jsonify(sqt.ratings_by_product(product))

@app.route("/newuser", methods=["POST"])
def insert_new_user():
    new_user = request.form.get("new_user")
    return str(sqt.insert_user(new_user))

@app.route("/newproduct", methods=["POST"])
def insert_new_product():
    new_product = request.form.get("new_product")
    return str(sqt.insert_product(new_product))

@app.route("/newrating", methods=["POST"])
def insert_new_rating():
    nuevo_rating = {"rating"       : request.form.get("rating")       ,
                    "rating_text"  : request.form.get("rating_text")  ,
                    "rating_title" : request.form.get("rating_title") ,
                    "date"         : request.form.get("date")         ,
                    "recommended"  : bool(request.form.get("recommended"))  ,
                    "Product_name" : request.form.get("Product_name") ,
                    "username"     : request.form.get("username")     }
    print(nuevo_rating)
    return str(sqt.insert_rating(nuevo_rating))




if __name__ == '__main__':
    app.run(debug=True)