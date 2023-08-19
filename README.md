# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. It demonstrates author's devops skills including AWS, designing and deploying infrastructure as code, monitoring CI/CD pipelines, and deploying scalable microservices using Kubernetes. It is an accumulation of many lessons I've learned.

This app converts an image from a format (e g. png, jpg, webp) to another. It runs on Kubernetes with docker. It uses AWS EKS for app hosting, and circleci for integration and deployment. It is also suited for local purposes. It's a great app if you need to convert an image on the go. 

## Current Plan and Progress

- Replace flask with FastAPI (Done)
- Apply unit testing (Done)
- Apply load testing using Locust swarm (Done)
- Convert server from monolith to microservices (Done)
- Add rate limiter to microservices (Done)
- Apply CI/CD using CircleCI (In Progress)
- Add integration testing for microservices (Done. Verified locally. Need to fix routing response in `microservices/gateway`)
- Apply Blue/Green Deployment
- Apply Prometheus and Grafana to microservice using Helm Chart
- Make it work 100% locally using Minikube (Done. Need to make sure local file path is returned instead of AWS S3 url when using local solution. This will be done in the future)
- Make this app is easy to start and use locally by ordinary people (In Progress)
- Finalize README.md. Nearly half of contents need update.
- Submit project

## Setup Instruction (General. Don't skip this step)

### Construct AWS S3 Storage

1. Login to [Amazon AWS Service](https://aws.amazon.com/)
2. Click `S3` from the intro dashboard

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/4275b9dd-4e09-4f66-8879-27edd8e60937"/>

3. Select `Create Bucket` on top right corner

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/80d7b0d2-7d86-4f2e-95ba-0882b0dedf1e"/>

4. Enter bucket name

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/8b88eb3c-523e-4444-9b86-878de1d26081"/>

5. Deselect `Block all public access`
    - This is to allow frontend program to access the url and offer converted image to client

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/31d6e3a8-ee90-4e68-ab2b-8171878d1806"/>

6. Scroll to the bottom and select `Create Bucket`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/c371427c-e0c0-4ae8-ada7-f118abdaab21"/>

### Get AWS S3 Access key and Secret Key

1. Login to [Amazon AWS Service](https://aws.amazon.com/)
2. Click `IAM` from the intro dashboard

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/01314857-6587-49a6-975d-4d728b2ad642"/>

3. Select `Users`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/962beb02-cff6-4169-a7bc-5ac085f29560"/>

4. Select `Add Users`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/0ff51061-29a1-4245-bf28-3d098291e0d5"/>

5. Type in `User name` (can be any. example: img-converter), and then click `Next`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/846abb6b-4c31-4fb9-bf41-994409e062a6"/>

6. Select `Attach Policies Directly`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/b3d7c018-6a6a-4324-ada5-6a4d0c8489e0"/>

7. In `Search` field, type `S3`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/a1b9b4bd-f078-4522-8f7f-c26ba6d5a963"/>

8. Select `AmazonS3FullAccess`, and click `Next` button

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/3fbe2205-b03d-4746-b1f6-07bf3889ce5b"/>

9. Select `Create User` button

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/ad56904a-4036-4966-a09c-9494545239c1"/>

10. Select newly created IAM User (in the author's case, img-converter-2)

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/34e99ad0-e86d-4482-a38f-4bbe19db5860"/>

11. Select `Security Credentials` tab

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/c82976ad-85d2-416b-848d-5d97067611c3"/>

12. Select `Create Access Key` button under `Access Keys`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/e61c5bb4-dadf-49bd-981d-4f660bd49f61"/>

13. Select `Other` and click `Next`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/fb9d9d3e-a1d5-42de-868d-f54e0522d20c"/>

14. Select `Create Access Key`

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/7c41a62c-af31-448f-8d9d-c329aaca9705"/>

15. Copy and paste respective value to respective variable in `.env` file

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/39dbe54a-8a76-4530-a741-4e454e9aed0c"/>

## Setup Instruction (Local)

### Install Docker

1. Please follow instruction from [here](https://docs.docker.com/get-docker/)

### Install Minikube

1. Please follow instruction from [here](https://minikube.sigs.k8s.io/docs/start)

### Run Program

1. Type `make start_minikube_local` in terminal from project root folder

## Setup Instruction (AWS)

### Setup Docker Hub

1. Sign up / sign in to [Docker Hub](https://hub.docker.com/)

### Setup CircleCI

### Fill Environment Variables in CircleCI

### Fork Repository
1. click `fork` on the top right corner of this [page](https://github.com/hyungmogu/udacity-cloud-devops-project-5/tree/main)

### Run CircleCI 

1. Sign up or sign in to [CircleCI](https://circleci.com)

## Test Instruction (Local)

### Unit Test
1. type `make test_local` in terminal to run unit tests

### Load Test
1. go to the project root folder
2. type `make setup_minikube` in terminal if not done.
3. fill out the following fields in `.env` file located in the project root folder.
    - "AWS_S3_BUCKET"
    - "AWS_ACCESS_KEY_ID"
    - "AWS_SECRET_ACCESS_KEY"
4. type `start_minikube_local` in terminal
5. In another tab, go to project root folder and type`make start_locust`
5. go to a browser of choice, and type "http://localhost:8089" in url.
6. in the input fileds enter as below:

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/67674efc-960e-4ba6-8636-0bd05fa2b3e2"/>

7. Click `Start Swarming` button

8. Click `Charts` to see activity as a graph

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/039ae455-eecc-4cb4-88e8-538083ec4cdb"/>

## Pipeline, and Diagrams

### Pipeline

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/4ec38587-9825-463f-8ef7-96b6184f6ff5"/>

### Basic Diagram

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/14dfd567-1f43-49b4-813e-e800dfcd195b"/> 

### Infrastructure Diagram

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/5200178e-dbaf-46c9-9e45-d59b27a3281e"/> 

### Requirements and Resource Estimation

#### Functional Requirements
1. Upload images to server
2. Convert images from original format to target format
3. Download converted images

#### Non-functional Requirements
1. High-availability: Target availability of 99% and higher.
2. Scalability: The following should not be bottleneck when scales
    1. Uploading images
    2. Viewing of website
    3. Downloading images

3. Performance: The conversion should be done as quick as possible, as additional delays will clog the system.

#### Resource Estimation
1. Estimated number of daily active users: 1 million (for demonstration purposes)
2. Max file size per image: 5MB (1280 x 960, png)
3. Max number of files submitted per user per day: 5

#### Number of servers estimation

- AWS EC2 Pricing information can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/)

- Est_number_of_servers_required = Daily_active_users / Server_daily_request_capacity == 1,000,000 / 86400 ~= 12 servers
    - This is based on conversative assumption that python-based server can handle [1 requests per second (1/12 of the original assumption made in this article)](https://news.ycombinator.com/item?id=26188765)


- Given `AWS t4g.medium` costs `$0.0336 server / hour`, it costs
    - `$24.192 server / month`
    - `$290.30 / month` for 12 servers

#### Bandwidth Usage Estimation (EC2)

- Assume the worst case scenario of image format conversion where size of the converted image triples (jpg -> png). That is 5MB -> 15MB.
- Data transfer to EC2 is free, so no calculation is required here
- Data transfer out of EC2, there is a charge, and it is:

```
15MB / file * 5 files * 1,000,000 = 75,000,000 MB  = 75 TB
```

Since AWS charges

1. `$0.09 / GB` for first 10 TB
2. `$0.085 / GB` for next 40 TB
3. `$0.07 / GB` for next 100 TB

The total outbound bandwidth cost is

```
$0.09 / GB * 10,000 GB + $0.085 / GB * 40,000 GB  + $0.07 / GB * 25,000 GB = $6050
```

#### Maximum total costs / month

The maximum total costs would be 

```
$290.30 / month + $6050 / month = $6340.30 / month
```

Of course, cost can be lowered using cheaper providers like Digital Ocean, but the conclusion here is that a sufficient revenue generating model other than google ad is required to keep this afloat.

Cost can be lowered using methods like keeping the converted files for only 1 hour. By doing this, the daily required storage reduces from 75 TB to 3 TB, and the cost decreases to $560.30 ($290.30 for AWS EC2 $270.00 for AWS s3). Still, for a solution that's as simple as converting an image format, $560.30 is a cost that's prohibitively expensive.

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
5. Ben Dilts, Karl Sun, et. al. (2023). Lucid chart - Where seeing becomes doing. Lucid.https://www.lucidchart.com/pages/landing
6. Benjamin Muschko. (2021). Certified Kubernetes Application Developer (CKAD) Study Guide: In-Depth Guidance and Practice 1st Edition. O'Reilly Publications.
7. Benjamin Muschko. (2022). Certified Kubernetes Administrator (CKA) Study Guide. O'Reilly Publications.
8. Bas Meijer, Lorin, Hochstein, Rene Moser. (2022). Ansible: Up and Running, Third Edition. O'Reilly Publications.
9. Ashley Davis. (2021). Bootstrapping Microservices with Docker, Kubernetes and Terraform. Manning Publications.
10. Imam Bux. (2020, Aug 4th). minikube ip is not reachable. Stack Overflow. https://stackoverflow.com/questions/60710171/minikube-ip-is-not-reachable#answer-63243909
11. Jeff Geerling. (2011). Ansible for DevOps. Leanpub.
12. Amazon. (2023). Auto Scaling Template Snippets. AWS. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-autoscaling.html
13. Andres. (05.03.2023). Multiple Playbooks in Ansible. dev.to. https://dev.to/andresfmoya/multiple-playbooks-in-ansible-2pdc
14. Build Virtual. Deploy a kubernetes cluster using ansible. Build Virtual. https://buildvirtual.net/deploy-a-kubernetes-cluster-using-ansible/
14. Troung. AWS S3: Bucket cannot have ACLs set with ObjectOwnership's BucketOwnerEnforced setting. Stack Overflow. https://stackoverflow.com/questions/76097031/aws-s3-bucket-cannot-have-acls-set-with-objectownerships-bucketownerenforced-s#76107203
15. Tamás Panyi. Build a Kubernetes Cluster on AWS with CloudFormation from Scratch. Medium. https://medium.com/@panyitamas/build-a-kubernetes-cluster-on-aws-with-cloudformation-from-scratch-d7ecfbed16a2
16. Ankit Gangwar. Setup Prometheus and Grafana monitoring on Kubernetes cluster using Helm. Medium. https://medium.com/globant/setup-prometheus-and-grafana-monitoring-on-kubernetes-cluster-using-helm-3484efd85891
17. The Kubernetes Authors. Configuring Redis using a ConfigMap. Kubernetes. https://kubernetes.io/docs/tutorials/configuration/configure-redis-using-configmap
18. Shahar Azulay. Redis on Kubernetes: A Powerful Solution – With Limits. groundcover. https://www.groundcover.com/blog/redis-cluster-kubernetes
19. Ferdinand de Antoni. Redis Cluster on Kubernetes. Medium. https://medium.com/geekculture/redis-cluster-on-kubernetes-c9839f1c14b6
20. Dragonfly DB. Error: redis.exceptions.responseerror moved. Dragonfly. https://www.dragonflydb.io/error-solutions/redis-exceptions-responseerror-moved
21. Anish. Kubernetes Access Service located in another namespace. 8gwifi. https://8gwifi.org/docs/kube-externalname.jsp
22. Kubernetes. Debugging DNS Resolution. kubernetes. https://kubernetes.io/docs/tasks/administer-cluster/dns-debugging-resolution/
23. JPG. How to add a custom decorator to a FastAPI route?. https://stackoverflow.com/questions/64497615/how-to-add-a-custom-decorator-to-a-fastapi-route
24. Mario. Building a Decorator for a Fastapi Route Simplify and Beautify Your App Routes. https://www.pythonbynight.com/blog/building-decorator-for-fastapi
25. Bubu Tripathy. Blue-Green Deployment using Kubernetes. https://medium.com/@bubu.tripathy/blue-green-deployment-using-kubernetes-be994df956b4
25. AWS Team. Why can't I connect to my Amazon EKS cluster?
. https://repost.aws/knowledge-center/eks-cluster-connection