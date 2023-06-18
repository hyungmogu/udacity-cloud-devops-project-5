# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. 

This app is about converting an image from a format (e g. png, jpg, webp) to another. It runs on kubernetes with docker. It uses AWS EKS for app hosting, and circleci for integration and deployment. It is also suited for local purposes.

This app is meant to demonstrate author's devops skills including AWS, designing and deploying infrastructure as code, monitoring CI/CD pipelines, and deploying scalable microservices using Kubernetes.

## Current Plan and Progress

- Replace flask with FastAPI (Done)
- Make it work 100% locally (Done)
- Apply unit testing (Done)
- Apply load testing using locust swarm (In Progress)
- Make sure this application works using minikube
  - [kompose](https://kompose.io) is used to convert from docker-compose.yml to kubernetes
- Convert server from monolith to microservice
- Apply CI/CD using circleci
- Deploy this app to AWS EKS via circleci
- Provide an easier way to setup and run locally
- Make sure this app works in all operating systems
- Submit project

## Setup Instruction (Local)

### Install Docker

1. Please follow instruction from [here](https://docs.docker.com/get-docker/)

### Run Program (backend)

1. Go to `backend` folder
2. type `make setup_local` if not done.
3. Type `make start` to run server

### Run Program (frontend)

1. Go to `frontend` folder

2. Type `make start` to run frontend program

## Setup Instruction (AWS)

## Test Instruction (Local)

### Unit Test
1. go to `backend` folder
2. type `make start_unit_test`

### Load Test
1. go to `backend` folder
2. type `make setup_local` if not done.
3. fill out the following fields in `.env` file located in the project root folder.
    - "AWS_S3_BUCKET"
    - "AWS_ACCESS_KEY_ID"
    - "AWS_SECRET_ACCESS_KEY"
4. type `make start_load_test`
5. go to a browser of choice, and type "http://localhost:8089" in url.
6. in the input fileds enter as below:

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/67674efc-960e-4ba6-8636-0bd05fa2b3e2"/>

7. Click `Start Swarming` button

8. Click `Charts` to see activity as a graph

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/039ae455-eecc-4cb4-88e8-538083ec4cdb"/>

## Pipeline, Architecture and System Design

<img src="https://user-images.githubusercontent.com/6856382/219821091-e647fe37-0c6f-40ec-a483-2ee99b91ae1d.png"/>

### Infrastructure Diagram

<img src="https://user-images.githubusercontent.com/6856382/229294233-491937b2-ad4b-4a22-af8c-f3bb5666fa20.jpeg"/> 

### Kubernetes Cluster Diagram

<img src="https://user-images.githubusercontent.com/6856382/229297085-f003ce51-4c14-4879-843d-4c30682aabd0.jpeg"/>

### Requirements and Resource Estimation

#### Functional Requirements
1. Uploading images from frontend (user) to client
2. Converting image from original format to target format
3. Downloading completed images

#### Non-functional Requirements
1. High-availability: Target availability of 99% and higher.
2. Scalability: The following should not be bottleneck when scales
    1. Uploading images
    2. Simulatenous viewing of website
    3. Downloading images

3. Performance: The conversion should be done as quick as possible, as additional delays will clog the system.

#### Resource Estimation
1. Estimated number of daily active users: 1 million (for demonstration purposes)
2. Max file size per image: 5MB (1280 x 960, png)
3. Max number of files submitted per user: 5
4. Max number of times a user could use this service a day: 5
5. Max size of an image after conversion: 12MB (From 5MB, jpg -> png)

#### Number of servers estimation

- AWS EC2 Pricing information can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/)

- Est_number_of_servers_required = Daily_active_users / Server_daily_request_capacity == 1,000,000 / 5,000 = 200 servers

- Given `AWS t4g.medium` costs `$0.0336 server / hour`, it costs
    - `$24.192 server / month`
    - `$4838.40 / month` for 200 servers

#### Bandwidth Usage Estimation (EC2)

- Data transfer in to EC2 is free, so no calculation is required here
- Data transfer out of EC2, we use

```
12MB / file * 5 files * 1,000,000 = 60,000,000 MB  = 60 TB
```

Since AWS charges

1. `$0.09 / GB` for first 10 TB
2. `$0.085 / GB` for next 40 TB
3. `$0.07 / GB` for next 100 TB

The total outbound bandwidth cost is

```
$0.09 / GB * 10,000 GB + $0.085 / GB * 40,000 GB  + $0.07 / GB * 10,000 GB = $5000
```

#### Maximum total costs / month

The maximum total costs would be 

```
$4838.40 / month + $5000 / month = $9838.40 / month
```

Of course, cost can be lowered using cheaper providers like Digital Ocean, but the conclusion here is that a sufficient revenue generating model other than google ad is required to keep this afloat.

## API Design

1. Convert To JPG

```
convertToJPG(image)
```

2. Convert To PNG

```
convertToPNG(image)
```

3. Convert To WEBP

```
convertToWEBP(image)
```

<table>
    <tbody>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>image</td>
            <td>Image that's being uploaded to server</td>
        </tr>
    </tbody>
</table>

## Project Rubric

### Setup Pipeline

1. Create Github repository with project code.
    - All project code is stored in a GitHub repository and a link to the repository has been provided for reviewers.

2. Use image repository to store Docker images
    - The project uses a centralized image repository to manage images built in the project. After a clean build, images are pushed to the repository.


### Build Docker Container

1. Execute linting step in code pipeline
    - Code is checked against a linter as part of a Continuous Integration step (demonstrated w/ two screenshots)

2. Build a Docker container in a pipeline
    - The project takes a Dockerfile and creates a Docker container in the pipeline.

### Successful Deployment

1. The Docker container is deployed to a Kubernetes cluster
    - The cluster is deployed with CloudFormation or Ansible. This should be in the source code of the student’s submission.

2. Use Blue/Green Deployment or a Rolling Deployment successfully
    - The project performs the correct steps to do a blue/green or rolling deployment into the environment selected. Submit the following screenshots as evidence of the successful completion of chosen deployment methodology:

        - a. Screenshot of the Circle CI or Jenkins pipeline showing all stages passed successfully.
        - b. Screenshot of your AWS EC2 page showing the newly created (for blue/green) or modified (for rolling) instances running as the EKS cluster nodes.
        - c. Screenshot of the kubectl command output showing that the deployment is successful, pods are running, and the service can be accessed via an external IP or port forwarding.
        - d. Screenshot showing that you can access the application after deployment.

## References

1. The Kompose Authors. (2022). Go from docker compose to kubernetes. https://kompose.io/
2. Udacity. (2023). Cloud DevOps Engineer Nanodegree. https://www.udacity.com/course/cloud-dev-ops-nanodegree--nd9991
3. Jonatan Heyman, Carl Byström, Joakim Hamrén, Hugo Heyman. (2023). Locust - An open source load testing tool. https://locust.io
4. Ashley D. (2021). Bootstrapping Microservices with Docker, Kubernetes and Terraform. Manning Publications Co.
