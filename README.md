# Flask Tasks
This service allows to create tasks with a command to be executed on background.

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Docker
- Docker Compose

### Running the service
Clone the repository
```
git clone git@github.com:FedericoJurio/flasktasks.git
```

Access to the project directory
```
cd flasktasks
```

Build the containers
```
docker-compose build
```

Run the containers
```
docker-compose up -d
```

## Documentation
This project follows the standard suggested by the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification) and generates the specification through [apispec](https://apispec.readthedocs.io/en/latest/) which is consumed by [Flasgger](https://github.com/flasgger/flasgger) and exposed in [http://localhost:8000/apidocs](http://localhost:8000/apidocs)
