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
- Apply Blue/Green Deployment (In Progress)
- Apply Prometheus and Grafana to microservice using Helm Chart
- Make it work 100% locally using Minikube (Done. Need to make sure local file path is returned instead of AWS S3 url when using local solution. This will be done in the future)
- Make this app is easy to start and use locally by ordinary people (In Progress)
- Finalize README.md. Nearly half of contents need update. (In progress)
- Fix errors (In Progress)
- Submit project

## Setup Instruction (Local)

### Install Docker

1. Please follow instruction from [here](https://docs.docker.com/get-docker/)

### Install Minikube

1. Please follow instruction from [here](https://minikube.sigs.k8s.io/docs/start)

### Run Program

1. Type `make start` in terminal from project root folder

## Setup Instruction (AWS)

### Activate AWS IAM access key 

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
1. Type `make test_unit` in terminal to run unit tests

### Load Test
1. Go to the project root folder
2. Type `make setup_minikube` in terminal if not done.
3. Fill out the following fields in `.env` file located in the project root folder.
    - "AWS_S3_BUCKET"
    - "AWS_ACCESS_KEY_ID"
    - "AWS_SECRET_ACCESS_KEY"
4. Type `make start_minikube` in terminal, and wait until minikube fully starts
5. In another tab, go to project root folder and type`make start_locust`
5. Go to a browser of choice, and type "http://localhost:8089" in url.
6. In the input fileds enter as below:

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/67674efc-960e-4ba6-8636-0bd05fa2b3e2"/>

7. Click `Start Swarming` button

8. Click `Charts` to see activity as a graph

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/039ae455-eecc-4cb4-88e8-538083ec4cdb"/>

## Pipeline, and Diagrams

### Pipeline

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/fbbb66f6-fc0b-424a-94d0-0c52a55bb3cc"/>

### Basic Diagram

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/14dfd567-1f43-49b4-813e-e800dfcd195b"/> 

### Infrastructure Diagram

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/5200178e-dbaf-46c9-9e45-d59b27a3281e"/> 

### Kubernetes Diagram

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/7b3dbd35-b3ba-492e-a54c-848043b91e2c"/>

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

- AWS Pricing information can be found [here](https://calculator.aws/#/addService)

- Est_number_of_servers_required = Daily_active_users / Server_daily_request_capacity == 1,000,000 / 86400 ~= 12 servers
    - This is based on conversative assumption that python-based server can handle [1 requests per second (1/12 of the original assumption made in this article)](https://news.ycombinator.com/item?id=26188765)


- Given `AWS t4g.medium` costs `$0.0336 server / hour`, it costs
    - `$24.192 server / month`
    - `$290.34 / month` for 12 servers

- AWS EKS costs `$73.00` per month

#### Bandwidth Usage Estimation (AWS)

- Assume the worst case scenario of image format conversion where size of the converted image triples (jpg -> png). That is 5MB -> 15MB.
- Data transfer to EC2 is free, so no calculation is required here
- Data transfer out of EC2, there is a charge. The calculation is as follows:

```
15MB / file * 5 files * 1,000,000 = 75,000,000 MB  = 75 TB
```

Since AWS charges

1. `$0.023 / GB` for first 50 TB
2. `$0.022 / GB` for next 450 TB

The total outbound bandwidth cost is

```
$0.023 / GB * 50,000 GB + $0.022 / GB * 25,000 GB = $1700
```

#### Maximum total costs / month

The maximum total costs would be 

```
$290.34 / month + $1700 / month + $73 / month = $2063.34 / month
```

Cost can be lowered using methods like keeping the converted files for only 1 hour. By doing this, the daily required storage reduces from 75 TB to 3 TB, and the cost decreases to $432 / month ($290.34 / month for AWS EC2 $69 / month for AWS S3, $73 / month for AWS EKS). Still, for a solution that's as simple as converting an image format, $432.34 / month is a cost that's prohibitively expensive.

Cost can be further lowered using cheaper providers like Digital Ocean, but the conclusion here is that running a microserivce is expensive, and unless a person is willing to handle the expense personally, a sufficient revenue generating model other than google ad is required to keep this afloat.

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
26. Giant Swarm. Using Kubernetes LoadBalancer Services on AWS. Medium. https://medium.com/@GiantSwarm/using-kubernetes-loadbalancer-services-on-aws-5c22f932d0c9
27. Meysam. How to Set Up Ingress Controller in AWS EKS. Medium. https://towardsdatascience.com/how-to-set-up-ingress-controller-in-aws-eks-d745d9107307
28. Kubernetes. Ingress. Kubernetes. https://kubernetes.io/docs/concepts/services-networking/ingress/
29. AWS EKS Workshop. Microservices on Kubernetes. Amazon Web Services. https://www.eksworkshop.com/docs/introduction/getting-started/microservices/
30. Peter De Tender. Setting up SSL/TLS for Kubernetes Ingress. snyk. https://snyk.io/blog/setting-up-ssl-tls-for-kubernetes-ingress/
31. Michael Pratt. Ingress vs. Load Balancer in Kubernetes. Baeldung. https://www.baeldung.com/ops/kubernetes-ingress-vs-load-balancer
32. Yang Yang and Michael Hausenblas. Kubernetes Ingress with AWS ALB Ingress Controller. AWS. https://aws.amazon.com/blogs/opensource/kubernetes-ingress-aws-alb-ingress-controller/
33. Kubernetes Team. Ingress-Nginx Controller Installation Guide. Kubernetes. https://kubernetes.github.io/ingress-nginx/deploy/
34. Elton Stoneman. (2021). Learn Kubernetes in a Month of Lunches. Manning Publications Co.
35. NGINX Team. Configure Rate Limiting. NGINX. https://docs.nginx.com/nginx-service-mesh/tutorials/ratelimit-walkthrough/#:~:text=In%20a%20Kubernetes%20environment%2C%20rate,workloads%20running%20inside%20the%20cluster.
36. Mike Petersen. Ultimate Guide to Kubernetes Ingress Controllers. Platform 9. https://platform9.com/blog/ultimate-guide-to-kubernetes-ingress-controllers/
37. Harsh Manvar. Kubernetes Ingress Vs Gateway API. https://medium.com/google-cloud/kubernetes-ingress-vs-gateway-api-647ee233693d
38. Dawid Kruk. How to create nginx ingress rules for services in 3 different namespaces in azure Kubernetes cluster. https://stackoverflow.com/questions/73918866/how-to-create-nginx-ingress-rules-for-services-in-3-different-namespaces-in-azur#answer-73921798