# Casting Agency

## Introduction
This project demonstrated the backend of a casting agency company that is responsible for creating movies and managing actors. With the API Movies & Actors can be created, listed, updated and deleted. There are three general roles within the company: a Casting Assitant, a Casting Director and an Executive Producer with different permissions that are explained in a chapter below. Each Movie has a title and release date and each actor has a name, an age and a gender. Both, Actors & Movies have an unique id.

## Tech Stack used in the project
The API was built using the programming language `python` and the webframework `flask`.
The Databasemanagementsystem used is PostgreSQL.

## Installation instructions, Installation of the dependencies
To run the application localy the following steps have to be followed:

#### 1. Fork & Pull or Clone the Githup repo into a local directory / repo.
One way to do this is to enter the following command:
```
  git clone https://github.com/Paweyyy/UdacityCapstoneFullStack
```

#### 2. Create & activate a virtual environment
```
  python3 -m venv myvenv
  source myvenv/bin/activate
```

#### 3. Create database & update setup.sh file
Create the database:
```
  createdb postgres
```

Make sure Database url in the `setup.sh` file is correct and includes the user credentials for your database and run:
```
chmod +x setup.sh
source setup.sh
```

### 4. Install required libraries

```
pip install -r requirements.txt
```

### 5. Run the database migration
```
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

### 6. Run the application
`python app.py`

## Testing instructions
The `CastingAgency.postman_collection.json`-File should be used for testing the endpoints using Postman. (https://www.postman.com)
All access tokens & test definitions for each role are already embedded into the file. For testing the following steps have to be followed:
1. Install Postman
2. Import the json.file / collection by clicking the "Import"-Button
3. Run the whole collection

## Roles and the permissions associated with it
Auth0 is used for security and authentication of the api. The authentication and authorization of a user works with JWT tockens that must include the permissions of a user and be included in the request header. There are three roles with different permissions that are described in the following:

### Casting Assistant
`read:actors` Can view actors

`read:movies` Can view movies

### Casting Director
`read:actors` Can view actors

`read:movies` Can view movies

`create:actors` Can create actors

`delete:actors` Can delete actors

`update:actors` Can update actors

`update:movies` Can update movies

### Executive Producer
`read:actors` Can view actors

`read:movies` Can view movies

`create:actors` Can create actors

`delete:actors` Can delete actors

`create:movies` Can create movies

`delete:movies` Can delete movies

`update:actors` Can update actors

`update:movies` Can update movies

## API Endpoints

### Public Endpoints
NONE - The whole API is fully protected and can only be accessed by authorized users.

### Protected Endpoints

#### GET /movies

Explenation: Fetches a dictionary of movies with ids, titles and release dates aswell as the total count of movies and a success variable
Request Arguments: `None`
Roles with access permissions: Casting Assistants, Casting Directors, Executive Producers

Sample response:
```
{
    "count": 1,
    "movies": [
        {
            "id": 14,
            "release_date": "Fri, 25 Dec 2020 11:12:13 GMT",
            "title": "New Movie"
        }
    ],
    "success": true
}
``` 

#### GET /actors

Explenation: Fetches a dictionary of actors with ids, name, age and gender aswell as the total count of movies and a success variable
Request Arguments: `None`
Roles with access permissions: Casting Assistants, Casting Directors, Executive Producers

Sample response:
```
{
    "count": 1,
    "actors": [
        {
            "age": 10,
            "gender": "male",
            "id": 2,
            "name": "George Clooney"
        }
    ],
    "success": true
}
``` 

#### POST /movies

Explenation: Creates a new movie.
Request Arguments: a JSON formatted object with the following keys: `title`, `release_date`
Roles with access permissions: Executive Producers

Sample response:
```
{
    "movies": [
        {
            "id": 14,
            "release_date": "Fri, 25 Dec 2020 11:12:13 GMT",
            "title": "New Movie"
        }
    ],
    "success": true
}
``` 

#### POST /actors

Explenation: Creates a new actor.
Request Arguments: a JSON formatted object with the following keys: `age`, `gender`, `name`
Roles with access permissions: Casting Directors, Executive Producers

Sample response:
```
{
    "actors": [
        {
            "age": 10,
            "gender": "male",
            "id": 2,
            "name": "George Clooney"
        }
    ],
    "success": true
}
``` 

#### UPDATE /movies/int:movie_id

Explenation: Updates an existing movie.
Request Arguments: URL Parameneter movie_id to specify which movie should be updated and a JSON formatted object with the at least one of the following keys: `title`, `release_date`
Roles with access permissions: Casting Directors, Executive Producers

Sample response:
```
{
    "movies": [
        {
            "id": 14,
            "release_date": "Fri, 25 Dec 2020 11:12:13 GMT",
            "title": "New Movie"
        }
    ],
    "success": true
}
``` 

#### UPDATE /actors/int:actor_id

Explenation: Updates an existing actor
Request Arguments: URL Parameneter actor_id to specify which actor should be updated and a JSON formatted object with the at least one of the following keys:  `age`, `gender`, `name`
Roles with access permissions: Casting Directors, Executive Producers

Sample response:
```
{
    "actors": [
        {
            "age": 10,
            "gender": "male",
            "id": 2,
            "name": "George Clooney"
        }
    ],
    "success": true
}
``` 

#### DELETE /movies/int:movie_id

Explenation: Deletes an existing movie.
Request Arguments: URL Parameneter movie_id to specify which movie should be deleted
Roles with access permissions: Executive Producers

Sample response:
```
{
    "id": 1,
    "success": true
}
``` 

#### DELETE /actors/int:actor_id

Explenation: Updates an existing actor
Request Arguments: URL Parameneter actor_id to specify which actor should be deleted
Roles with access permissions: Casting Directors, Executive Producers

Sample response:
```
{
    "id": 1,
    "success": true
}
``` 


## Heroku Link
The web application is hostet at: https://udcapstone.herokuapp.com/


