
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

For each space in Cloud.gov:

1. Log in to your Cloud.gov account and target the appropriate org and space:

   ```bash
   cf target -o <org-name> -s <space-name>
   ```

2. Create a PostgreSQL service instance:

   ```bash
   cf create-service aws-rds <database_type> <service-instance-name>
   OR 
   run create_cloudgov_service.sh
   ```

### Deploying the Flask Application

1. Ensure you have a `manifest.yml` and `vars.yml` file configured for your Flask application. The `vars.yml` file should include variables such as `FLASK_APP` and database service bindings.

2. Deploy the application using Cloud Foundry's `cf push` command with your variable file:

   ```bash
   cf push --vars-file vars.yml
   ```

#### To-Do: 
setup github workflow for commit, deployment. 
