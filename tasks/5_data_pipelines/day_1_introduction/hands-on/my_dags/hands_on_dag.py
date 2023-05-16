from datetime import datetime, timedelta

from airflow import DAG
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    "depends_on_past": False,
    "start_date": datetime(2022, 12, 12),
    "retries": 0,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    dag_id="hands_on_dag",
    default_args=default_args,
    catchup=False,
)


join_data = SparkSubmitOperator(
    task_id="join_data",
    # TODO: enter connection id you created in the UI
    # conn_id=""
    # TODO: enter path to the join_data script
    # application="",
    name="join_data",
    dag=dag,
    # TODO: enter path to the data folder
    # application_args=[""],
)

transform_data = SparkSubmitOperator(
    task_id="transform_data",
    # TODO: enter connection id you created in the UI
    # conn_id=""
    # TODO: enter path to the transform_data script
    # application="",
    name="transform_data",
    dag=dag,
    # TODO: enter path to the data folder
    # application_args=[""],
)
# Declare task dependencies: transform_data cannot run until join_data has finished
join_data >> transform_data
