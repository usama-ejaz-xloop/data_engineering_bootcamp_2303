# Module 4 day 1 hands-on: Data Pipeline in Apache Airflow


# Introduction

During this hands-on, your task will be to build and execute a data pipeline in Apache Airflow. In Airflow,
pipelines are defined using so called **DAG**s (Directed Acyclic Graphs). Each DAG consists of one or more **tasks**.
In our case, those tasks will be executed in PySpark.

# Tasks
## 1. Set up Apache Airflow

### Install required dependencies
```shell
pip install  pyspark
pip install "apache-airflow==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-<YOUR_PYTHON_VERSION>.txt"
# <YOUR_PYTHON_VERSION> is major python version you're using in your virtual environment. This can be checked by
# running python --version. If the result is e.g. 3.10.8, replace <YOUR_PYTHON_VERSION> with 3.10
pip install apache-airflow-providers-apache-spark
```

### Set the environment variable `AIRFLOW_HOME`
It will be used by airflow to create configuration files and log directory
```shell
export AIRFLOW_HOME=~/airflow
```

### Initialize the metadata database
```shell
airflow db init
```

### Point dags_folder to location in your project
Navigate to `~/airflow/airflow.cfg` and set `dags_folder` to `<PATH_TO_YOUR_REPOSITORY>/tasks/4_data_pipelines/day_1_introduction/hands-on/my_dags`.
This tells Airflow where to look for DAG definitions.

### Create admin user that will be used to manage Airflow UI:
```shell
airflow users create --username admin --firstname admin --lastname admin --role Admin --email admin --password admin
```

### Run Airflow Webserver in detached mode so that it can work in the background
```shell
airflow webserver -D
```

### Run Airflow Scheduler.
It monitors all tasks and DAGs, then triggers the task instances once their dependencies are complete.
```shell
airflow scheduler
```

### Navigate to [0.0.0.0:8080]() and log into the UI using admin credentials

### Set up Spark connection
From the Navbar in the UI, navigate to Admin > Connections and click the plus sign to add your own connection.
In `Connection id` enter `my_spark_connection`, choose Spark `Connection Type` and in `Host` field enter `local[*]`

## 2. Fill out missing values in the DAG skeleton

Pass correct arguments to DAG and task definitions.

## 3. Implement pipeline tasks

### Create a task responsible for reading and merging the data

Using files `movies.csv`, `ratings.csv` and `links.csv` create and save a DataFrame, that will contain the information
about ratings from users with ids from 1 to 10. Resulting DataFrame is supposed to have the following columns:

`imdbId | title | genres | userId | rating | date_time`


### Create a task responsible for transforming the data so that helpful conclusions can be drawn

Using DataFrame created by the `join_data` task, perform the following actions:
- convert `date_time` column so that it contains date objects
- group the data by ratings' count, so that you know how many movies were given each particular score (0.5, 1.0, ..., 5.0)
- calculate the average score for user with `userId` 1
- answer the question: "What are the imdbIds of the 10 movies with the highest average rating?"

## 4. Schedule tasks

Set up a schedule, so that the pipeline runs every 4 minutes.

