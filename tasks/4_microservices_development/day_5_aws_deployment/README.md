# Module 4 - Day 5 - Introduction to AWS

## Intro

During this hands-on exercise you will familiarize yourself with
the [AWS Management Console](https://aws.amazon.com/console/).

Also, you will set up a few basic services and mechanisms that are available for use on
AWS.

### Prerequisites

Be sure to have a working AWS user account and access
to [AWS Management Console](https://aws.amazon.com/console/).

### Hands-on plan

- [Main AWS Management Console elements](#main-aws-management-console-elements)
- [Creating an AWS User account](#creating-an-aws-user-account)
- [Creating a budget and budget alerts](#creating-a-budget)
- [Creating an IAM role](#creating-an-iam-role)
- [Creating a S3 Bucket & Uploading a file](#creating-a-s3-bucket-&-uploading-a-file)
- [Creating an EC2 instance](#creating-an-ec2-instance)

## Main AWS Management Console elements

### Service menu and search bar

In the top left part of the console page, you can access the service menu. Next to the
menu is the search bar.
You can use these sections to access the service pages - if
you're unclear what you're looking for, the service menu offers categories which contain
the relevant services.

Try selecting one of the categories (e.g. `Compute`) and inspect the presented services
and their descriptions.

### CloudShell, notifications, help menu, region selection, account details and settings

In the top right part of the console page, you can see a few icons and dropdowns.

Starting from the left, these are:

#### CloudShell

This is a service allows you to interact with the cloud using a web shell and an AWS
command line tool - which functions identically
to [AWS CLI](https://aws.amazon.com/cli/).

Open the CloudShell terminal and run `aws help` to see the help section and all
available options and services. (Press `Q` to exit the help section.)

#### Notifications

Here you will see all new notifications from AWS. You can select any of the sections to
open a more in-depth view of the messages.

#### Help

Here you can access support and documentation to help with using AWS.
These links will take you to external resources - we strongly advise you to use this
section, especially the documentation part.

#### Region selection

Here you can select the region that you'll be operating in - this should be left as
default - `us-east-1`.

In most cases, you will be working in the scope of a single region.

#### Account details and settings

This menu contains information about the account settings, billing, account security,
etc.

When developing on AWS, you won't be concerned with most of the sections besides
the **Security credentials** section.

In the security section, you do things like:

- see your user account details,
- change your password,
- set up MFA,
- generate access keys,

and more.

Feel free to explore this section a little, but be sure **not to change** the
existing configuration.

## Creating an AWS user account

To create a new AWS user account:

1. Use the search bar to go to `IAM` service.
2. Select `Users` from the menu on the left.
3. Click the `Add users` button on the top right side of the page.
4. Follow the dialog to create the user.
    - Set a name for the user: e.g., `<your name><first letter of your surname>`.
    - In credential type, select `Password`.
5. Users need to be a part of a group - these groups govern the access that the users
   have to AWS services.
    - You can select an existing group or create a new one. Attach the user to a
      group. (**Note**: You can assign a user to multiple groups).
6. Skip the `Tags` section
7. In the last section, you can review the whole operation and finalize it.

After the creation is finished, you can access the credentials to the account by either:

- downloading the csv file with the credentials,
- viewing the password on this page,
- sending an email with the credentials to the interested party.

Try using the account you just created to sign in to AWS.

**Bonus:** To delete the user account, select it in the IAM/Users section and click
the `Delete` button on the top right side. Follow the dialog to finalize the operation.

## Creating a budget

Budgets can be used to monitor spending on the given AWS account.

To create a new AWS budget:

1. Use the search bar to go to `Billing` section.
2. Select `Budgets` from the menu on the left.
3. Click the `Create budget` button on the top right side of the page.
4. Follow the dialog to create the budget.
    - Choose `Use a template` - `Monthly cost budget`.
    - Provide a budget name and an email for notifying if the budget is exceeded.
5. Click `Create budget` on the bottom to finalize the operation.

You can now select your newly created budget plan to see such statistics as:

- a forecast of the spending for future months
- detailed spending history and diagrams

Explore this section further to familiarize yourself with the possibilities of this
section.

## Creating an IAM role

IAM Roles can (and should) be used to manage access to AWS resources for entities such
as AWS users and other AWS resources.

Roles have a defined set of access permissions with short-lived credentials. Entities
assume the given role to have these permissions granted to them so that they're able to
perform some operations.

To create a new IAM role:

1. Use the search bar to go to `IAM` service.
2. Select `Roles` from the menu on the left.
3. Click the `Create role` button on the top right side of the page.
4. Follow the dialog to create the role. (In our case, we will create a role to use with
   a service called `EC2`. This role will be used in the later part of the exercise.)
    - Select `AWS service` and `EC2` as a trusted entity and use case.
    - Provide a budget name and a list of emails for notifying if the budget is
      exceeded.
    - Use the search bar to find and attach a policy called `AmazonS3FullAccess` by
      ticking the box next to it. This policy allows for full access to files stored on
      S3 (Simple Storage Service).
    - Provide a role name.
5. Click `Create role` on the bottom to finalize the operation.

You can now view this role in the IAM/Roles page.

The role is now ready to be used by the EC2 service to access other AWS services.

## Creating a S3 Bucket & Uploading a file

### Creating a bucket

S3 stands for Simple Storage Service - it is service for storing, accessing and
versioning files of any type.

To create a new EC2 instance (vm):

1. Use the search bar to go to `S3` service.
2. Click the `Create bucket` button on the top right side of the page.
3. Follow the dialog to create the instance.
    - Provide a bucket name - `<your name><first letter of your surname>-aws-handson`.
    - Leave all the other options on default.
4. Click `Create bucket` on the bottom right to finalize the operation.

### Uploading a file

Now we're ready to upload a file to the newly created bucket:

1. Create a text file called `<your name><first letter of your surname>-file.txt`. Edit
   the file to contain some message, e.g.: "Hello, I'm stored on S3!".
2. Go to your bucket and select `Upload`.
3. Select the file you created using the `Add files` button.
4. Click `Upload` on the bottom right to finalize the operation.

Now it should be possible for you to view your file on S3.

Extra: To download the file, just select it and click `Download`.

## Creating an EC2 instance

### Creating and connecting to the instance

EC2 stands for Elastic Compute Cloud - it is a compute platform service for creating
virtual machines in the cloud. These can be used as any other virtual machine - as a
remote development environment, a server, etc.

To create a new EC2 instance (vm):

1. Use the search bar to go to `EC2` service.
2. Select `Instances` from the menu on the left.
3. Click the `Launch instances` button on the top right side of the page.
4. Follow the dialog to create the instance.
    - Provide an instance name.
    - Select `Ubuntu` as the OS image.
    - Select `t2.micro` instance type.
    - In the next section, click on `Create new key pair`.
        - Provide a name for the keypair and create it (we will use this to connect to
          the EC2 instance) - this will download the keypair file.
    - Select the newly created keypair.
5. Click `Launch instance` on the right to finalize the operation.

After a while, the EC2 instance will be ready to use. You can now go back to the
instance list to see your new instance's status and details.

To connect to the instance via
SSH ([Secure Shell](https://pl.wikipedia.org/wiki/Secure_Shell)), select your EC2
instance and click on the `Connect` button on the top. Select the `SSH client` section
and do the following:

1. Open a terminal session locally and navigate to the location where you keypair file
   is downloaded.
2. Change the access permission to the keypair file by running the following command:

```shell
chmod 400 <your_keypair_file_name>.pem
```

3. Run the command under the `Example` line on the AWS page to connect to the instance.
   This would something like that:

```shell
ssh -i "johns_keypair.pem" ubuntu@ec2-12-345-6-789.compute-1.amazonaws.com
```

4. Enter "yes" to continue connecting to your instance.

After these steps, you should be connected to your EC2 instance and can start working on
the next part of the exercise.

### Working on the instance

Install the AWS CLI tool on your EC2 instance using the following command:

```shell
sudo snap install aws-cli --classic
```

You'll try to view and download the file you uploaded to S3 in the previous step of the
exercise.

Try viewing all the buckets on the cloud using the following command:

```shell
aws s3 ls
```

You should see an error that the tool cannot find the AWS credentials on the machine.

To solve this, we need to attach the IAM role (that has full S3 access) that we
previously created to the EC2 instance to give the EC2 instance required permissions to
interact with S3. This is one of the use cases of the IAM roles - to allow AWS services
to interact with one another.

To attach the role:

1. Go to the `EC2` service console.
2. Select your instance and then select `Actions → Security → Modify IAM role`
3. Select the role that you've previously created.
4. Click `Update IAM role`  to finalize the operation.

Now you're ready to go back to your EC2 instance. Try to execute the command again - it
should execute successfully, and you should see a list of S3 buckets:

```shell
aws s3 ls
```

**Note**: All S3 paths must start with `s3://` and a bucket name.

To view all the files on your bucket, use the following command:

```shell
aws s3 ls s3://aws-hands-on-bucket
```

To download the file to the machine, use the following command:

```shell
aws s3 cp s3://aws-hands-on-bucket/<your_file_name>.txt ./<your_file_name>.txt
```

Using the `cp` command, you need to provide the path on the S3 bucket to the file and
the path on your local machine that the file will be saved to.

Use the following command to view the file contents:

```shell
cat <your_file_name>.txt
```

You should see the message you wrote in the file previously. This concludes the
exercise.

**NOTE: After you're done with the exercise, be sure to stop the
instance in the `EC2/Instances` page.**

This can be done by selecting the instance and selecting
the `Stop instance` option from the `Instance state` dropdown. This will prevent you
from incurring additional costs, as the instance will **not** stop automatically.
