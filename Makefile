.PHONY: all build clean copy-src local setup test up update-dependencies

CKAN_HOME := /srv/app

all: build

# ###############################################
# Core commands
# ###############################################

build:
	docker-compose build --parallel

clean:
	docker-compose down -v --remove-orphans

up:
	docker-compose up $(ARGS)


# ###############################################
# Test commands
# ###############################################

db-up:
	docker-compose up -d db

test: db-up
	poetry run pytest