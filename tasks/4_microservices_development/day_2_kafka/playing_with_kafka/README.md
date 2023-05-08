# Playing with Kafka
Start Kafka with:

```
docker-compose up -d
```

Create a topic using:

```
./create_kafka_topic.sh events
```

Listen to events via:

```
docker exec -ti broker kafka-console-consumer \
	--topic events \
	--bootstrap-server broker:9092
```

And, in a separate terminal, send some events via:

```
docker exec -ti broker kafka-console-producer \
	--topic events \
	--bootstrap-server broker:9092
```

Write the events in the terminal, separating with a newline.

