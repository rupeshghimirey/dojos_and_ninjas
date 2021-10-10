from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

# ==============================================
# Show Home Route that redirects to dojos
# ==============================================
@app.route("/")
def index():
    return redirect('/dojos')

# ==============================================
# Register Page
# ==============================================
@app.route("/register-page")
def reggister():
    list_of_all_dojos = Dojo.get_all_dojos();

    return render_template("register.html", all_dojos = list_of_all_dojos)

# ==============================================
# Login
# ==============================================
@app.route("/login-page")
def login():
    list_of_all_dojos = Dojo.get_all_dojos();

    return render_template("login.html", all_dojos = list_of_all_dojos)

# ==========================================
# Route that shows the create_dojos html page
# contains form for adding new dojos
# ==========================================
@app.route("/dojos")
def add_dojo_page():
    # call the get all classmethod to get all users

    list_of_all_dojos = Dojo.get_all_dojos();

    return render_template("create_dojos.html", all_dojos = list_of_all_dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "name": request.form["name"],
    }
    # We pass the data dictionary into the save method from the Dojo class.
    id = Dojo.save(data)
    path = "users" + "/" + str(id)
    print(id)
    # Don't forget to redirect after saving to the database.
    return redirect('/dojos')

# ==========================================
# Route that takes the id from a href, we are
# passing it to the class method name 
# ==========================================

@app.route("/dojos/details/<int:dojo_id>")
def dojo_details_with_ninja(dojo_id):
    data = {
        "dojo_id" : dojo_id
    }
    dojo_one = Dojo.get_one_dojo_with_ninja(data)
    return render_template("dojo_details.html", dojo_one = dojo_one)


