#!/bin/sh

set -e 

# If an argument was provided, use it as the service name prefix. 
# Otherwise default to "harvesting-logic".
app_name=${1:-harvesting-logic}

# Get the current space and trim leading whitespace
space=$(cf target | grep space | cut -d : -f 2 | xargs)

# Production and staging should use bigger DB instances
if [ "$space" = "prod" ] || [ "$space" = "staging" ]; then
    cf service "${app_name}-db"    > /dev/null 2>&1 || cf create-service aws-rds medium-psql-redundant "${app_name}-db" --wait&
else
    cf service "${app_name}-db"    > /dev/null 2>&1 || cf create-service aws-rds micro-psql "${app_name}-db" --wait&
fi
