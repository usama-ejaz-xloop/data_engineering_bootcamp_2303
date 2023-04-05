#!/bin/bash

docker rm -f postgres

docker run --name postgres -p 5432:5432 -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -d postgres

sleep 5

docker exec -it postgres psql --user postgres -c "CREATE DATABASE test;"
docker exec -it postgres psql --user postgres -d test -c \
    "CREATE TABLE people(id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255));"
docker exec -it postgres psql --user postgres -d test -c \
    "INSERT INTO people(first_name, last_name) VALUES ('John', 'Smith'), ('Mary', 'Smith');"

