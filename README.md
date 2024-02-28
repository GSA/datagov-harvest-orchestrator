
# DataGov Harvest Orchestrator

The DataGov Harvest Orchestrator is a Flask-based application specifically developed to oversee and facilitate the data harvesting process. It is equipped to manage basic Create, Read, Update, and Delete (CRUD) operations for Harvest Source configurations and to initiate harvest jobs efficiently.

## Project Dependency Management with Poetry

This project uses [Poetry](https://python-poetry.org/) for dependency management. To set up the project:

1. Ensure Poetry is installed.

2. Clone the repository and navigate to the project directory:

3. Install dependencies using Poetry:

   ```bash
   poetry install
   ```

## Development

### Environment Setup

1. Copy the sample environment file and set your local configurations:

   ```bash
   cp .env.sample .env
   ```

   Edit the `.env` file with your local settings.

### Running the Application

1. Use the Makefile to set up local Docker containers, including a PostgreSQL database and the Flask application:

   ```bash
   make build 
   make up
   make test
   make clean
   ```

   This will start the necessary services and execute the test.

## Deployment to cloud.gov

### Database Service Setup

### Harvesting Logic Database

A database service is required for use on cloud.gov.

In a given Cloud Foundry `space`, a db can be created with `cf create-service <service offering> <plan> <service instance>`. In dev, for example, the db was created with `cf create-service aws-rds micro-psql harvesting-logic-db`. Creating databases for the other spaces should follow the same pattern, though the size may need to be adjusted (see available AWS RDS service offerings with `cf marketplace -e aws-rds`).

Any created service needs to be bound to an app with `cf bind-service <app> <service>`. With the above example, the db can be bound with `cf bind-service harvesting-logic harvesting-logic-db`.

Accessing the service can be done with service keys. They can be created with `cf create-service-keys`, listed with `cf service-keys`, and shown with `cf service-key <service-key-name>`.

### Deploying the Flask Application

1. Ensure you have a `manifest.yml` and `vars.yml` file configured for your Flask application. The `vars.yml` file should include variables such as `FLASK_APP` and database service bindings.

2. Deploy the application using Cloud Foundry's `cf push` command with your variable file:

   ```bash
   cf push --vars-file vars.yml
   ```

#### To-Do: 
setup github workflow for commit, deployment. 
