from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/add_ninja")
def add_ninja_page():

    list_of_all_dojos = Dojo.get_all_dojos();
    # call the get all classmethod to get all users
    return render_template("add_ninja.html", list_of_all_dojos=list_of_all_dojos)

@app.route('/add_ninja', methods=["POST"])
def create_User():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"]
    }
    Ninja.save(data)
    
    return redirect("/dojos")