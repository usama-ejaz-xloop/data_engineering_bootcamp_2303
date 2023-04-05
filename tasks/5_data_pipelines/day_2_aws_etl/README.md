# Data Pipelines

## Day 2 - ETL Processes in AWS

This hands-on will be focused on implementing an ETL process using AWS Glue and its
visual editor.

The step-by-step explanation of the tasks can be found in the paragraphs below and in
the
slides at the end of the presentation file.

## Task 0 - Draw conclusions

**During the execution of the whole exercise, please formulate thoughts and prepare
notes about which service serves which role in the ETL process.**

**For each exercise step and used service, answer the questions:**

- Why do we need to take this step?
- What is this service's purpose?

**Try to assign each of the used services to the three ETL stages.**

## Task 1 - Data access preparation

Prepare the data sources for processing using AWS Glue.

### S3

Go to S3 service console and create a new S3 bucket
called `<your name><your surname>-glue-data` - for
example, `johnsmith-glue-data`.

In this bucket, create three directories:

- `glue_data` - for glue intermediate data
- `input_data` - for our input CSV data
- `output_data` - for our output Parquet data

In the `glue_data` directory, create two directories:

- `scripts`
- `temp`

In the `input_data` directory, create the directories as
follows: `earnings/date=<today's date> (yyyy-mm-dd)` -
an example structure would look like
that: `johnsmith-glue-data/input_data/earnings/date=1970-01-11`.

Select the `date=<today's date>` directory and upload the `earnings_1.csv` file to it -
it
can be found in the code repository, in the `data` folder of today's exercise.

### RDS

Go to RDS service console, select `Databases → Create database`.

Choose:

- Creation method: `Standard create`
- Engine options:
    - Engine type: `PostgreSQL`
    - Engine version: `Default (as is)`
- Templates: `Free tier`
- Settings:
    - DB instance identifier: `<your name><your surname>-employees-db`
    - Master username: `<your name><your surname>`
    - Master password: `mod4day2empl` - confirm password
- Storage:
    - Allocated storage: change to `20GB`
    - Uncheck `Enable storage autoscaling`
- Connectivity:
    - In `Public access` section, select `Yes`
- Performance Insights:
    - Uncheck `Turn on Performance Insights`
- Additional configuration:
    - Initial database name: `employees_db`
    - Database options: Uncheck `Enable automated backups`
    - Encryption: Uncheck `Enable encryption`
    - Maintenance: Uncheck `Enable auto minor version upgrade`

Check your configuration and click `Create database`.

The creation of the database takes a few minutes, in the meantime we can create some
other resources for the database, crawlers and Glue to use.

#### IAM Roles

Go to IAM service console, select `Roles` on the left hand side.

Select `Create role`. Under the `Use case` section, choose `Glue` from the selection.
In the next section, search for `AmazonS3FullAccess` and `AWSGlueServiceRole` and add
both of
these policies.
In the final section, name the role as `<your name><your surname>-glue-role`.

Create the role - this will be used by Glue to access the data and perform the ETL job.

#### VPC Endpoint

Go to VPC service console, select `Endpoints` on the left hand side.

Select `Create endpoint`. Search for `s3` and select `com.amazonaws.us-east-1.s3` of
type  `Gateway`.
In the next section, select the default VPC. Finally, check the only available route
table to be used by the endpoint.
Under the `Policy` section, `Full access` should be selected.

Click on `Create endpoint` to finalize.

#### Security group rules

Navigate to your newly created RDS database when it's done creating and then go
to `Security group rules` section.

Here you can see two rules, one inbound, one outbound, both belonging to a default
`Security group`. Select this group and then click on the `Security group ID`. Here you
can inspect security rules for this group - we need to add two inbound rules. Click
`Edit inbound rules` and add the following:

- Rule for Glue Crawler access to RDS DB:
    - Type: `All TCP`
    - Source: `Custom` (Here select the default security group ID, same as rule above)
    - Description: `Rule for Glue Crawler`
- Rule for access to RDS DB from our python script:
    - Type: `PostgreSQL`
    - Source: `Anywhere - IPv4`
    - Description: `Rule for external access`

Click on `Save rules` to finalize.

#### Populate the database

**Note: To continue with this task, the RDS database you've created and deployed
earlier must be available. Check the deployment status of the database and make sure it
is ready.**

Navigate to [populate_db.py](./populate_db.py) script in the repository. Fill out the
DatabaseConnector class
constuctor call with your information. You can find the `host` endpoint URL in the
connectivity
section in your RDS database details.

Run the following commands locally, in the repository's exercise directory:

```shell
sudo apt install python3-dev
sudo apt install libpq-dev
pip install -r requirements.txt
python3 populate_db.py
```

The data should now be accessible in RDS.

## Task 2 - ETL in Glue

Prepare the Glue crawlers and job constituting the ETL process.

### Data Catalog Database

Go to Glue service console, select `Databases` on the left hand side.

Select `Add database` with the following parameters:

- Name: `<your name><your surname>_glue_database`

Click on `Create database` to finalize.

### Glue Crawlers

You need to prepare two crawlers, since we have two data sources - S3 and RDS.

#### RDS Crawler

Go to Glue service console, select `Crawlers` on the left hand side.

Select `Create crawler` with the following parameters:

- Name: `<your name><your surname>_rds_employees_crawler`
- Add a data source: `JDBC`
    - While creating the data source, you have to create a database connection:
        - Name: `<your name><your surname>_glue_rds_connection`
        - Connection type: `Amazon RDS`
        - Database engine: `PostgreSQL`
        - In the next section, select the database you've created previously and supply
          the password (should be `mod4day2empl`)
        - After you're done creating the connection, select it as a data source in the
          Glue Crawler dialog
- Include path: `employees_db/public/employees`
- IAM role:
    - Existing IAM role: Select the IAM role that you've created in Task 1
- Output configuration:
    - Target database: Select the Glue Data Catalog Database that you've created
    - Table name prefix: `<your name><your surname>_`

Go to the next section to create the crawler.

#### S3 Crawler

Go to Glue service console, select `Crawlers` on the left hand side.

Select `Create crawler` with the following parameters:

- Name: `<your name><your surname>_s3_earnings_crawler`
- Add a data source: `S3`
    - S3 path: choose `<bucket>/input_data/earnings`
- IAM role:
    - Existing IAM role: Select the IAM role that you've created in Task 1
- Output configuration:
    - Target database: Select the Glue Data Catalog Database that you've created
    - Table name prefix: `<your name><your surname>_`

Go to the next section to create the crawler.

After both of the crawlers are created, select them and click `Run`. This will create
tables
in the Glue Data Catalog that we can use as inputs for your Glue job.

### Glue Job

Go to Glue service console, select `Jobs` on the left hand side.
Select `Visual with a blank canvas` and click `Create`.

#### Data Source Nodes

Here we have to add two data sources nodes - one for RDS, one for S3.

Use Glue Data Catalog tables as source types for both of these nodes. One source type
should be S3, and the other - Relational DB. You can view all the available data source
node types in the `Source` dropdown on the top left side of the editor

You can view the data schema in the `Output schema` section of these nodes.

#### Transform Nodes

Use the `Rename field` action to rename the `emp_id` field to `rds_emp_id` in the data
from
the RDS data source.

Use the `Join` action to merge the two data sources on employee ID.

Use the `Change Schema(Apply Mapping)` to:

- Rename the `emp_id` key to `employee_id`
- Rename the `date` key to `earnings_date`
- Change the data types so that they are correct (`ints/floats` for numerical, `date`
  for dates, etc.)
- Swap all the spaces in the keys names to underscores ( _ )
- Drop the `rds_emp_id` key
- Rename/drop the fields as you see fit

#### Data Output Nodes

Select the `Data Target - S3` action from the menu. Set the following parameters:

- Format: `Parquet`
- Compression Type: `Snappy`
- S3 Target Location: `<your_bucket>/output_data/employees_earnings/`
- Data Catalog update
  options: `Create a table in the Data Catalog and on subsequent runs, update the schema and add new partitions`
- Database: Your created Glue database
- Table name: `<your name><your surname>_employees_earnings`
- Partition keys: choose `earnings_date`

#### Job Details

Navigate to the `Job Details` section. Set the following parameters:

- **Basic properties:**
    - Job name: `<your name><your surname>_employee_earnings_job`
    - IAM Role: Your created Glue role
    - Check `Automatically scale the number of workers`
    - Maximum number of workers: `3`
    - Job bookmark: `Disable` (in case of errors and re-runs)
    - Number of retries: `0`
- **Advances properties:**
    - Script filename: `<your name><your surname>_employees_earnings.py`
    - Set the `Script path` to the `scripts` S3 directory created in Task 1
    - Uncheck `Spark UI`
    - Set the `Temporary path` to the `temp` S3 directory created in Task 1

#### Saving & Running the job

Save the job with the button in the top-right corner. After the job is saved, run the
job.
You can view all the job runs in the `Runs` section of the editor.

After the job is marked as completed in the `Runs` section, check the S3
bucket's `output_data` directory for the outputted results - it should be a bunch of
Parquet files in a date partitioned directory.

## Task 3 - Additional data

In the `input_data` directory, create the directories as
follows: `earnings/date=<tomorrow's date> (yyyy-mm-dd)` -
an example structure would look like
that: `johnsmith-glue-data/input_data/earnings/date=1970-01-11`.

Select the `date=<tomorrow's date>` directory and upload the `earnings_2.csv` file
to it - it can be found in the code repository, in the `data` folder of today's
exercise.

Rerun the S3 crawler and the job. A new partition with tomorrow's date should appear
in the S3 bucket's  `output_data` directory that contains the new data.

## Bonus task:

Brainstorm: Check if it is possible to run the jobs and crawlers automatically when new
data in S3/RDS
appears. How would you go about implementing this mechanism?