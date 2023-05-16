# Running PySpark examples in Jupyter Lab

We'll run our Spark examples using official
`jupyter/pyspark-notebook` Docker image. In order to run a container based on this image, execute:
```shell
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```
This command will run a container and provide you with the link to Jupyter Lab workspace. Paste this link into your
browser, and you're good to go!

In order to run the example, when in your Jupyter Lab workspace, copy the file `spark_example.ipynb` into `work/` folder.
Then, create `data/` folder and upload files `store_1.csv` and `store_2.csv` there. You should now be able to run the
example notebook