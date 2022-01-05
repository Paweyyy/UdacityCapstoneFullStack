import os
from flask import Flask, json, jsonify, abort, request
from models import setup_db, Actor, Movie
from flask_cors import CORS
from datetime import datetime

from auth import AuthError, requires_auth

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app, ressources={ r"*/api/*": { "origins": '*' }})

    #################################
    #### Actors
    #################################

    #### GET
    @app.route("/actors", methods=["GET"])
    #@requires_auth("read:actors")
    def get_models():
        actors = Actor.query.all()
        formateed_actors = [actor.format() for actor in actors]
        return jsonify({
            "success": True,
            "actors": formateed_actors,
            "count": len(formateed_actors)
        })


    ### POST
    @app.route("/actors", methods=["POST"])
    @requires_auth("create:actors")
    def create_actor():
        body = request.get_json()
        new_name = body["name"]
        new_age = body["age"]
        new_gender = body["gender"]

        if new_name is None or new_age is None or new_gender is None:
            abort(404)

        actor = Actor(name=new_name, age=new_age, gender=new_gender)
        actor.insert()

        return jsonify({
            "success": True,
            "actors": [actor.format()]
        })

    ### PATCH
    @app.route("/actors/<int:actor_id>", methods=["PATCH"])
    @requires_auth("update:actors")
    def update_actor(actor_id):
        body = request.get_json()

        if actor_id is None:
            abort(404)

        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor is None:
            abort(404)

        if "age" in body.keys():
            actor.age = body["age"]

        if "gender" in body.keys():
            actor.gender = body["gender"]

        if "name" in body.keys():
            actor.name = body["name"]

        return jsonify({
            "success": True,
            "actors": [actor.format()]
        })

    #### DELETE
    @app.route("/actors/<int:actor_id>", methods=["DELETE"])
    @requires_auth("delete:actors")
    def remove_actor(actor_id):
        body = request.get_json()

        if actor_id is None:
            abort(404)

        actor = Actor.query.filter_by(id=actor_id).one_or_none()

        if actor is None:
            abort(404)

        id = actor.id

        actor.delete()

        return jsonify({
            "success": True,
            "id": id
        })


    #################################
    #### Movies
    #################################

    #### GET
    @app.route("/movies", methods=["GET"])
    @requires_auth("read:movies")
    def get_movies():
        movies = Actor.query.all()
        formateed_movies = [movie.format() for movie in movies]
        return jsonify({
            "success": True,
            "actors": formateed_movies,
            "count": len(formateed_movies)
        })


    ### POST
    @app.route("/movies", methods=["POST"])
    @requires_auth("create:movies")
    def create_movie():
        body = request.get_json()
        print(request.get_json())
        new_title = body["title"]
        new_release_date = body["release_date"]

        if new_title is None or new_release_date is None:
            abort(404)

        new_converted_release_date = datetime.strptime(new_release_date, '%d/%m/%y %H:%M:%S')
        print(new_converted_release_date)
        movie = Movie(title=new_title, release_date=new_converted_release_date)
        movie.insert()

        return jsonify({
            "success": True,
            "movies": [movie.format()]
        })

    ### PATCH
    @app.route("/movies/<int:movie_id>", methods=["PATCH"])
    @requires_auth("update:movies")
    def update_movie(movie_id):
        body = request.get_json()

        if movie_id is None:
            abort(404)

        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        if movie is None:
            abort(404)

        if "title" in body.keys():
            movie.title = body["title"]

        if "release_date" in body.keys():
            movie.release_date = datetime.strptime(body["release_date"], '%d/%m/%y %H:%M:%S')

        return jsonify({
            "success": True,
            "movies": [movie.format()]
        })

    #### DELETE
    @app.route("/movie/<int:movie_id>", methods=["DELETE"])
    @requires_auth("delete:movies")
    def remove_movie(movie_id):
        body = request.get_json()

        if movie_id is None:
            abort(404)

        movie = Movie.query.filter_by(id=movie_id).one_or_none()

        if movie is None:
            abort(404)

        id = movie.id

        movie.delete()

        return jsonify({
            "success": True,
            "id": id
        })
        
    #################################
    #### ERROR HANDLERS
    #################################


    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False, 
            "error": 404, 
            "message": "resource not found"
        }),404

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False, 
            "error": 400, "message": "bad request"
        }), 400

    @app.errorhandler(500)
    def bad_request(error):
        return jsonify({
            "success": False, 
            "error": 500, 
            "message": "internal server error"
        }), 500

    @app.errorhandler(AuthError)
    def authentication_error(error):
        code = error.get_status_code()
        err = error.get_error()
        print(code, err)
        return jsonify({
            "success": False,
            "error": err,
            "decription": code
        }), code

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
