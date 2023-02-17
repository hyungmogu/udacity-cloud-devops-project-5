# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. 

## Scope of the project

- CircleCI will be used for Continuous Integration phase
- Blue / Green Deployment will be used
- Application from project 3 is used
- Backend Program of the application from project 3 will be dockerized for use in this project
- Ansible and Cloudformation will be used to build infastructure
- Kubernetes cluster will be built from scratch on AWS
- Kubernetes cluster will be initialized using Ansible and Cloudformation

## Pipeline Plan

<img src="https://user-images.githubusercontent.com/6856382/219556274-b7af7630-d8b7-42e8-804a-8e2a72b71928.png"/>

## Kubernetes Cluster Infrastructure Diagram

<img src="https://user-images.githubusercontent.com/6856382/219568785-bd6acabb-ed19-497a-849c-96bdcbd7baa8.png"/> 

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

