# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. It demonstrates author's devops skills including AWS, designing and deploying infrastructure as code, monitoring CI/CD pipelines, and deploying scalable microservices using Kubernetes. It is an accumulation of many lessons I've learned.

This app converts an image from a format (e g. png, jpg, webp) to another. It runs on Kubernetes with docker. It uses AWS EKS for app hosting, and circleci for integration and deployment. It's an app to go if a user wants to convert images.

## Setup Instruction

### 1) Create AWS IAM access key

1. Please follow the guide provided [here](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html)
    -  If this is first time, please create user first by following the instruction below, after clicking this link [here](https://console.aws.amazon.com/iam/)
    - Please download or write down access key for the use in step 5

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/c70f63bd-4d69-4864-b617-e73f3caf2ea2"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/df3a6c42-d626-4b13-859e-e6bc3aaa139a"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/9c53c6e0-095b-42d4-8b0a-a03034a85713"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/76a211cb-bb10-478e-afaa-4ec541b2cc22"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/ca1acc27-7b60-4418-98dc-c2d529150087"/>

### 2) Create AWS S3 Bucket

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/2c30160d-df65-49cf-b48b-d5325e945e6c"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/85f45af8-b664-450f-9552-8d139b4711a7"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/af9c3725-12f8-498a-b5bd-98c6aa6cb9fd"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/af9c3725-12f8-498a-b5bd-98c6aa6cb9fd"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/48196060-cc18-4d77-aecd-1d7433139c66"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/5dba1693-a777-4ca8-85cc-80739d9bdb66"/>

### 3) Attach S3FullAccess Policy to IAM user

-  Please follow the instruction below, after clicking this link [here](https://console.aws.amazon.com/iam/)

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/fe517f19-562c-4a84-b518-0fbd713abe64"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/02dc4040-4395-4f46-9fd2-869cf4c24bb3"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/b75fd4f7-e690-40ba-bfc0-a7f534b7d006"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/2edb9119-b1d3-4706-8f13-965a56dcce9d"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/a403b03e-0c68-471d-89ce-80b4dfb20c34"/>

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/351086a7-06d7-4e90-b8b4-20c92c7958b5"/>

### 4) Setup Docker Hub

- a. Please sign up / sign in to [Docker Hub](https://hub.docker.com/)
    - **Note:** Please sign up using random and secure passwords. This will help increase user protection from unexpected circumstances.

### 5) Setup Github

- a. Please sign up / sign in to [Github](https://github.com/)
    - **Note:** Please sign up using random and secure passwords. This will help increase user protection from unexpected circumstances.

- b. Please fork, or clone and then re-upload this repository to user's github.

### 6) Setup CircleCI

- a. Please sign up or sign in to [CircleCI](https://circleci.com)
    - **Note:** Please sign up using random and secure passwords. This will help increase user protection from unexpected circumstances.

- b. Please link this CircleCI account to signed-in Github account from step 3

### 7) Fill Environment Variables in CircleCI

- a. Please follow the instruction provided below, after clicking this link [here](https://circleci.com):

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/5350bd51-2736-4f07-a9c7-19a7c618cf02">

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/51399fd0-aa83-448a-8012-6ee27dfbec6b">

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/762dbb43-2c6a-4838-87bd-eec0c4a23803">

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/6e1cf2f2-6904-4a1f-a434-b948733483a0">

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/652c02ab-f469-4133-8f5d-82c996b586ca">

<img src="https://github.com/hyungmogu/udacity-cloud-devops-project-5/assets/6856382/e7aed042-107c-42c9-8917-0afb6da310a2">

### 8) Make a Commit, and Start CICD!

- a. Please add space or an extra character to this README.md, and make a commit. This will trigger CircleCI, and start executing a build.

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
39. Awanish. Building a Kubernetes Application with Amazon EKS. Medium. https://medium.com/edureka/amazon-eks-ac646c23abf8
40. AWS Team. Clean Up. AWS. https://archive.eksworkshop.com/beginner/130_exposing-service/cleaning/
41. Digital Ocean Team. How to Delete Load Balancers from Kubernetes Clusters. Digital Ocean. https://docs.digitalocean.com/products/kubernetes/how-to/delete-load-balancers
42. ElmoVanKielmo. What is the meaning of "gaierror: [Errno -3] Temporary failure in name resolution". Stack Overflow. https://stackoverflow.com/questions/40238610/what-is-the-meaning-of-gaierror-errno-3-temporary-failure-in-name-resolutio#answer-40238730