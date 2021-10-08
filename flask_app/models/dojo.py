from werkzeug.utils import redirect
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls,data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES(%(name)s, NOW(), NOW());"
        return connectToMySQL('dojos_and_ninjas').query_db(query,data)


# ==========================================================
# GET METHOD, method that returns the list of the dojos
# ==========================================================
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('dojos_and_ninjas').query_db(query)
        # Create an empty list to append our instances of friends
        dojos = []
        # Iterate over the db results and create instances of friends with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one_dojo_with_ninja(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(dojo_id)s"
        results = connectToMySQL('dojos_and_ninjas').query_db( query, data)

        dojo = cls(results[0])

        for row_data in results:
            ninja_data = {
            "id" : row_data["ninjas.id"],
            "first_name"  : row_data["first_name"],
            "last_name"   : row_data["last_name"],
            "age"         : row_data["age"],
            "dojo_id"     : row_data["dojo_id"],
            "created_at"  : row_data["ninjas.created_at"],
            "updated_at"  : row_data["ninjas.updated_at"]
            }

            dojo.ninjas.append(ninja.Ninja(ninja_data));
        return dojo;
