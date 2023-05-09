# Python Microservice Development
## Day 3 - Kubernetes
This directory contains files related to minor task and hands-on part for day 3 of the module as well as `play_with_kubernetes/apply_kubernetes_object` directory with an example from presentation (to submit a deployment to Kubernetes cluster).

The detailed explanation of the tasks can be also found in the slides at the end of the presentation file.

In these exercises we are going to use `minikube` and `kubectl` commands. Please see the syntax of the latter:
```
kubectl [command] [TYPE] [NAME] [flags]
```

### Task 1
1. Your task is to create two services: a `MongoDB` database and mongo-express
2. Write configuration files for these services and their deployments
3. Apply them to the Kubernetes cluster with `kubectl apply -f <configuration_file_name>`


### Task 2
Your task is to expose the `mongo-express` service from the last exercise.
1. Ensure Service is a type of LoadBalancer and assign NodePort in Service specifications.
2. Because we use Minikube, after applying changes to the Kubernetes cluster we have to do an additional step and type:
```
minikube service <service_name>
```
To create `MongoDB` and `mongo-express` deployments we used env variables as plain text inside the configuration file. Think about which data should be protected in `Secret` and which may be stored inside `ConfigMap`. Change `Deployment` specification to use Secret and `ConfigMap`.

### Hands-on task
We will use the images you created on the first day of the Microservices module. This time however you will use the Kubernetes cluster to manage your services. Your task is to integrate the frontend and the inference module into a full app that detects objects on an image.

#### Hint
To make local images of `frontend` and `inference` usable in Deployment definition there is some more adjustment needed.
We are not going to use Docker images from image registry neither global or local. Thus we need to follow the steps to allow this:
1. Run `eval $(minikube docker-env)` in the terminal to reuse the Docker demon from Minikube.
2. Open another terminal session
3. Build the `frontend` and `inference` image once again: `docker build -t my-image .` .
4. Set `imagePullPolicy` to `Never` - we are not going to pull data from registry.
5. Apply your Kubernetes manifest.
6. Expose service with Minikube.