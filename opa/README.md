# demo

## Introduction

Repository demonstrates launching two simple services:

- a REST endpoint receiving a given username and role
- an OPA service evaluating the access rights for a given username and role

Once set up, the user can query access rights as follows:

    curl --location --request POST "https://my-cool-service:8000/api/user-access" --header 'Content-Type: application/json' --data-raw '{ "Username": "joe", "role": "admin" }'

## Setup

Following setup was verified on a Windows 10 machine.

Generate a self-signed certificate:

    openssl req -x509 -newkey rsa:4096 -keyout app/key.pem -out app/cert.pem -days 365 -nodes -subj '/CN=my-cool-service'

Build and tag each Docker Image

    docker build -t kubernetes/frontend:demo app
    docker build -t kubernetes/backend:demo security

Load the local images into Minikube.

    minikube image load kubernetes/frontend:demo
    minikube image load kubernetes/backend:demo

Apply the configuration files:

    kubectl apply -f kubernetes

Run the following to expose the port on localhost:

    kubectl port-forward svc/app-service 8000:80

Keep the terminal open.

### Running the code

If the _frontend_ needs to be resolved by hostname, add it to your _hosts_ file.

The container defined as _tester_ in docker-compose.yml does this automatically, by resolving it as _host-gateway_.

Evaluating True:

    curl --location --request POST "https://my-cool-service:8000/api/user-access" --header 'Content-Type: application/json' --data-raw '{ "Username": "joe", "role": "admin" }'
    curl --location --request POST "https://my-cool-service:8000/api/user-access" --header 'Content-Type: application/json' --data-raw '{ "Username": "jane", "role": "manager" }'

Evaluating False:

    curl --location --request POST "https://my-cool-service:8000/api/user-access" --header 'Content-Type: application/json' --data-raw '{ "Username": "joe", "role": "user" }'
    curl --location --request POST "https://my-cool-service:8000/api/user-access" --header 'Content-Type: application/json' --data-raw '{ "Username": "", "role": "admin" }'

Alternatively, run the pytests:

    pytest --url https://my-cool-service:8000 test

### TODO / Not-in-scope / limitations

- Using a production server
- Proper testing (pytest was written _very_ quickly)
- Best practices regarding command/entrypoint split between Dockerfile & Kubernetes configuration (?)
- Clear split of variable/path/url ownership/definition
- Organization could be better
