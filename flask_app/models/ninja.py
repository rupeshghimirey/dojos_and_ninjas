from werkzeug.utils import redirect
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojo_id = data['dojo_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_ninja(form_data):
        is_valid = True;
        if (len(form_data['first_name'])) < 4:
            flash("Name must be atleast 4 characters long!")
            is_valid = False;
        if (len(form_data['last_name'])) < 4:
            flash("Name must be atleast 4 characters long!")
            is_valid = False;
        if len(form_data['dojo_id']) < 1:
            flash("Please select the location!")
            is_valid = False;
        if form_data['age'] == "":
            flash("Please enter a valid age!")
        elif int(form_data['age']) <18:
            flash("You must be atleast 18 years old to be a Ninja!")
            is_valid = False;
        
        return is_valid
        


    @classmethod
    def save(cls,data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojo_id, created_at, updated_at) VALUES(%(first_name)s,%(last_name)s,%(age)s, %(dojo_id)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)
        