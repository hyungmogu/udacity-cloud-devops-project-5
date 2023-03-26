# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. 

## Scope of the project

- Jenkins will be used for CI and CD
- Rolling Deployment will be used
- Cloudformation will be used to build infastructure
- Kubernetes cluster will be built from scratch on AWS
- Kubernetes cluster will be initialized using Ansible and Cloudformation

## Pipeline Plan

<img src="https://user-images.githubusercontent.com/6856382/219821091-e647fe37-0c6f-40ec-a483-2ee99b91ae1d.png"/>

## Deployment Architecture

<img src="https://user-images.githubusercontent.com/6856382/226086046-10f2ec21-c2fb-418d-aa1b-48557938969d.jpeg">

## Infrastructure Diagram

<img src="https://user-images.githubusercontent.com/6856382/227803683-a82f38ef-9086-40aa-9635-82251f4485a6.jpeg"/> 

## Kubernetes Architecture Diagram

<img src="https://user-images.githubusercontent.com/6856382/227812057-08f5265e-fac0-4014-ad28-6a5fce14e302.jpeg"/>

## Rubric

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

#
