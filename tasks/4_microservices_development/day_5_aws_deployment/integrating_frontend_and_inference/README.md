# Deploying microservices to AWS

During this hands-on, you will use your solution from day 1 of this module in order to
deploy two microservices to Amazon ECS using Fargate. One service will be responsible for the inference and is based on
the task originally placed in `/tasks/5_microservices_development/day_1_microservices/inference_api`
and the other one will be responsible for the front-end side and is based on the task `/tasks/5_microservices_development/day_1_microservices/dockerizing_front_end`.


In order to make our application visible to the world, we'll need to :
1. Create an AWS ECS cluster
1. See [this tutorial](https://linuxhint.com/create-ecs-cluster-aws/) if you have trouble finding it.
2. Setup Service Discovery
3. Build Docker images using provided Dockerfile and push them to Amazon Elastic Container Registry
4. Create task definitions for both front-end and inference, using built images
5. Create the ECS services
6. View your service


## 1. Create ECS Cluster
- From ECS Console, click `Create Cluster`, then choose option `EC2 Linux + Networking'. Besides cluster,
it creates necessary resources for us: VPC and Subnets
- Enter cluster name
- Leave all other options as default

## 2. Setup Service Discovery
Now, we need to set up Service Discovery. It enables the communication between multiple services working in the same VPC.
How it works is that you define your namespace and service, and then, when you reference those values in your code,
they are automatically translated into private IPs of services you want to target.
To set it ip:
- In AWS Console, open AWS Cloud Map service
- Click `Create Namespace`
- Choose a name for your namespace (e.g. `example.com`)
- In `Instance discovery`, choose `API calls and DNS queries in VPCs`
- In `VPC` choose the VPC that was created with your cluster
- Leave other options as default and click `Create namespace`
- When in newly created namespace, click `Create service`, choose a name (e.g. `inference`) and leave all other options as default.

## 3. Build and push Docker images to Amazon ECR
Before you begin building the images, look at Dockerfiles provided in `/flask_frontend/Dockerfile` and `/fastapi_/Dockerfile` and try to analyze each line and its meaning.

#### 1. Create ECR repository for each image
- In the AWS Console, navigate to `Elastic Container Registry`
- Click `Get Started` and then create a private repository. Name it `frontend`. Leave all other options as default.
- Repeat the previous step for the inference: create the repository and name it `inference`.
#### 2. Push your images to ECR
For both repositories, do the following:
- Open the repository in the Console, and from the right corner of the screen, click `View push commands'. You'll be
shown a list of commands that you'll need to execute in order to push the image.

#### ❗️NOTE: bear in mind, that when executing the `docker build -t <image_name> .` you need to be inside the directory that your Dockerfile is located.

## 4. Create task definitions
For both inference and frontend, do the following:
- From the ECS Console, navigate to `Task Definitions` and create new Fargate task definition
- For both task definitions specify task definition name, and amount of memory and CPU used by the task
(2GB for memory and 1vCPU will be sufficient)
- In the `Add container` section:
  - Specify container name and image URI (you can find it by opening your image in the ECR Console)
  - For the inference container:
    - In `Port mappings` section add port 8686
  - For the frontend container:
    - In `Port mappings` section add port 5000
    - In `Environment variables` section add new variable with key `SERVICE_DISCOVERY` and value from previously created
    Service Discovery: `<service_name>.<namespace_name>`. So for the namespace `example.com` and service `inference`,
    this value should be `inference.example.com`. This way we can reference this value in our frontend code:
    ```python3
    predictions_url = f"http://{os.environ['SERVICE_DISCOVERY']}:8686/inference"
    ```

## 5. Create the ECS services
From cluster menu, create two services: frontend and inference
- For both services, in the `Configure service` section:
  - choose FARGATE as launch type
  - Specify appropriate task definition, service name and number of tasks
- In the `Configure network` section
  - Use the VPC that was created for the cluster
  - Choose all available subnets
  - For frontend service:
    - Edit newly created security group: add inbound rule of type `Custom TCP` with port range 5000
  - For inference service:
    - Edit newly created security group: add inbound rule of type `Custom TCP` with port range 8686
    - In the `Service discovery` section, check `Enable service discovery integration`. Then, in `Namespace` section choose
    the namespace you created in Section 2. The same goes for service: click `Select existing service discovery service`
    and choose previously created service.

## 6. View your service

- Open your cluster and from `Services` choose your frontend service
- Navigate to `Tasks` and choose existing task
- Find the Elastic Network (ENI ID) attached to the task, and click it
- From the Network Interfaces list, choose the correct one, and open it
- Find `Public IPv4 DNS` for the ENI, copy it and paste it in the browser address bar, adding the port number 5000 in the end
  (e.g. `ec2-35-158-125-37.eu-central-1.compute.amazonaws.com:5000`)

## 7. Cleanup

After you have finished the exercise, delete the cluster along with all its resources
(they are present in cluster's CloudFormation stack) so that it won't generate unnecessary costs.
