# Daily assignment

### Set up

Run Jupyter Lab:
```shell
docker run -it --rm -p 8888:8888 jupyter/pyspark-notebook
```

Next, upload all the files into your Jupyter workspace, and recreate the folder structure:
```
data/
- store_transactions/
    - transactions_1.csv
    - transactions_2.csv
    - transactions_3.csv
- customers.csv
- products.csv
```

Then, in a notebook, find answers to the following questions:
### 1. What are the daily total sales for the store with id 1?
(To do this, join transactions from store 1 and products tables, multiply `Quantity` and `UnitPrice` columns and find the sum)
### 2. What are the mean sales for the store with id 2?
(To do this, join transactions from store 2 and products tables, multiply `Quantity` and `UnitPrice` columns and find the mean)
### 3. What is the email of the client who spent the most when summing up purchases from all of the stores?
### 4. Which 5 products are most frequently bought across all stores?
