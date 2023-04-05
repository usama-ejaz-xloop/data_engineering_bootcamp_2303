# Data Pipelines

## Day 3 - Apache Spark

During this day you will use Spark with various data sources for stream and batch processing. You will run local instances of Spark and Kafka. Finally, you will apply some data transformations in Jupyter notebook running Spark underneath.

## Prequisitions

### Prepare local Kafka

We will be reusing the local setup for Kafka from `tasks/5_microservices_development/day_2_kafka/playing_with_kafka/docker-compose.yml`. Docker Compose is used to define all necessary services for Kafka to run, such as ZooKeeper. Run all commands in the directory where this `README.md` file is located.

To start containers with Kafka and ZooKeeper run the following command in a console:
```bash
docker-compose -f ../../5_microservices_development/day_2_kafka/playing_with_kafka/docker-compose.yml up -d
```

We can use the script to create a Kafka topic and name it `events`:
```bash
../../5_microservices_development/day_2_kafka/playing_with_kafka/create_kafka_topic.sh events
```

After creating a topic we can listen to the events by running the following command executed directly in the Kafka container. If you run the command shortly after the services were created with Docker Compose, you might get warning messages. Just wait a few additional seconds, all services need some additional time to start.
```bash
docker exec -ti broker kafka-console-consumer \
	--topic events \
	--bootstrap-server broker:9092
```

Now we can test our local setup. The following command should be executed in a separate console window. This command will create a producer. The producer will allow us to send messages by simply writing them down in the console after running the command. Messages will be sent to the previously created topic. Check it out for yourself if the Kafka setup works as expected!
```bash
docker exec -ti broker kafka-console-producer \
	--topic events \
	--bootstrap-server broker:9092
```

### Prepare local Spark

We will use the Docker Hub image to run Spark locally with Jupyter notebook. To run the container execute the following command in a separate console window:
```bash
docker run \
	--network="host" \
	--user "$(id -u)" \
	--group-add users \
	--volume "${PWD}":/home/jovyan/workspace \
	jupyter/pyspark-notebook:1840ddc9dc35
```

You can find URL to access Jupyter lab in browser in logs from console window. URL should look like this: `127.0.0.1:8888/lab?token=<token>`

## Exercises and tasks

Run `workspace/tasks.ipynb` notebook. The notebook is split into two parts. In the first part, you will go through batch processing in Spark.

Before doing a second part with Spark Streaming, run the `workspace/exercises.ipynb` notebook. It provides a simple example of how to use Spark Streaming with Kafka.
