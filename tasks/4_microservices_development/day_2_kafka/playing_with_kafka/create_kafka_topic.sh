#!/bin/bash

docker-compose exec broker kafka-topics --create --topic events --bootstrap-server broker:9092
