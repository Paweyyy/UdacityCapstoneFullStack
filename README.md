# Casting Agency

## Introduction
This project demonstrated the backend of a casting agency company that is responsible for creating movies and managing and assigning actors to those movies. 

## Motivation behind the project


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

## Documentation of the APIs
## Heroku Link
The web application is hostet at: https://udcapstone.herokuapp.com/


