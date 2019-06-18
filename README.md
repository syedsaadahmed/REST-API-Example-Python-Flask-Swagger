# RESTFUL API Using Python Flask and Swagger UI


## A Brief Introduction

In last few years REST (REpresentational State Transfer) has been used as an architectural design for web services and web APIs. The REST architecture was originally designed to fit the HTTP protocol that the world wide web uses.
Central to the concept of RESTful web services is the notion of resources. Resources are represented by URIs. The clients send requests to these URIs using the methods defined by the HTTP protocol, and possibly as a result of that the state of the affected resource changes.

Building RESTFUL web services with Flask is quite simple. There are many Flask extensions that help with building RESTful services with Flask. In place of a database we will use a memory structure. it woyld work when the web server that runs our application is single process and single threaded. it is just to be used as example with Flask's own development web server. one must not use this technique on a production web server, proper database either SQL or No-SQL depends on the usage setup must be used instead.

Moreover we have used Swagger UI that allows anyone — be it your development team or your end consumers — to visualize and interact with the API’s resources without having any of the implementation logic in place.


## Pre-requisites

One must have Python installed in his local system for deploying this RESTFUL-API easily. Other than Python one must also have to install Python-Flask and its dependencies as mentioned in the requirements.txt file.


## Running the RESTFUL-API Service

using nohup (no hangup) 
```
nohup python server.py &
```

**You can also run the RESTFUL-API via Gunicorn**

```
gunicorn --workers 4 --access-logfile /var/tmp/gunicorn.logs --bind 0.0.0.0:5000 wsgi:app
``` 

**workers = 4 (The number of worker processes. This number should generally be between 2-4 workers per core in the server.)**

**access-logfile = path of the file, where logs are to be saved**

**bind = Specify a server socket to bind.**

It will deploy the web service, no need of andy manual or human intervention. 


## Checking the User Interface

https://localhost:5000/


# FEW ASPECTS RELATED TO RESTFUL-API

## Testing

Something that is untested is broken. Python Flask actually provides a way to test your application by exposing the Werkzeug test Client and handling the context locals for you. One can simply use a module named as PyTest for testing Flask web services and APIs
A little PyTest Flask example is being written here;

```
import pytest

from ex_app import my_app


@pytest.fixture
def app():
    app = my_app()
    return app

def test_example(client):
    response = client.get("/")
    assert response.status_code == 200


```

## Security

For security of our RESTFUL API, we can use mulitple options, which are provide by Python-flask like Flask-JWT tokens, Flask OAuth2 libraries, Moreover one can have route authentication and authorization implemented in his web service.
In short vast variety of fruitful solutions are there, it depends on scenario and infrastructure that how one must chose to secure the endpoints and routes present in web service.

## Scalibility

A three tier architecture for scaling REST API to a huge infrastructure must be useful, One must kept database and webserver at two different nodes, and in between them there should be a load balancer that will handle the bulk amount of requests coming to the API. In this all the requests must be successfully handled and your web service can be easily scaled to a bigger infra.

## Limitations

A issue you would probably face is that the server is single-threaded. This means that it will handle each request one at a time, serially. This means that if you are trying to serve more than one request, so the requests will take longer. If any given requests happens to take a long time (say, 20 seconds) then your entire application is unresponsive for that time (20 seconds). This is only the default, of course: you could bump the thread counts (or have requests be handled in other processes), which might alleviate some issues. But once again, it can still be slow under a "high" load. What is considered a "high" load will be dependent on your application and the expectations of a maximum acceptable response time.

Another issue is security: if you are concerned at ALL about security, then you should not use the development server. It is not ready to withstand any sort of attack.

Yes, you could still conceivably use it in production. And yes, I would still recommend using a "real" web server. If you don't like the idea of needing to install something like Apache or Nginx, you can still go with a solution that is still as easy as "run a python script" by using some of the WSGI Standalone servers, which can run a server that is designed to be in production with something just as simple as running python run_app.py in the command line.

## Documentation

This RESTFUL-API is written using Python-Flask, Huge, extensive and detailed documentation for flask is provided (http://flask.pocoo.org/docs/1.0/), Furthermore a very strong support is also there on multiple platform all around the web.

## Deployment

In the current scenario, Python-Flask own development web server is used to run the service. one must not use this technique on a production web server, Mulitple other web servers dedicated for running such type of service are present such as "Gunicorn" is a good example, we can also use "Apache" or "Nginx" for that. Also proper database either SQL or No-SQL depends on the usage setup must be used with the deployment.
