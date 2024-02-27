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

test: build
	# docker build -t ghcr.io/gsa/catalog.data.gov:latest ckan/
	docker-compose -f docker-compose.yml -f docker-compose.test.yml up --abort-on-container-exit test
