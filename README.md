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

## Kubernetes Cluster Diagram

<img src="https://user-images.githubusercontent.com/6856382/227823674-9c9da05c-e546-444d-bd41-62fa4f62d11f.jpeg"/>

## Requirements

### Functional Requirements
1. Uploading images from frontend (user) to client
2. Converting image from original format to target format
3. Downloading completed images

### Non-functional Requirements
1. High-availability: Target availability of 99% and higher.
2. Scalability: The following should not be bottleneck when scales
    1. Uploading images
    2. Simulatenous viewing of website
    3. Downloading images
    4. Image storage for conversion 

3. Performance: The conversion should be done as quick as possible, as additional delays will clog the system.

## Resource Estimation
1. Estimated number of daily active users: 1 million (for demonstration purposes)
2. Max file size per image: 5MB (1280 x 960, png)
3. Max number of files submitted per user: 5
4. Max number of times a user could use this service a day: 5
5. Max size of an image after conversion: 12MB (From 5MB, jpg -> png)

## Resource Estimation Constratints

1. Max time of withholding image data on storage: 15 minutes

## Storage Estimation
1. (1,000,000 users * 5 MB / file * 5 file / day) * (1 + 2.4) = 85 million MB = 85 TB / day

2. 85 TB / day ~= 59.027GB / minutes ~= 885 GB / 15 minutes

- Given the constraints, the amount of storage required is 885 GB.

- In AWS's S3, this roughly translates to $20 USD / month

## Bandwidth Estimation

- `upload:download` ratio is assumed to be 1 (meaning, for every upload, there is equivalent number of downloads)

### The bandwidth required for uploading videos

1. Total_bandwidth == Amount_of_files_uploaded_to_server_per_day * (day / 86400s) ==  1,000,000 user * 5 MB / file * 5 file / day ~= 0.28GB Gbps


```
(1,000,000 users / day * 5 MB / file * 5 file / day) * (1GB / 1000MB) * (day / 86400s) ~= 0.28GB / s
```

### The bandwidth required for downloading videos

- More info: [here](https://aws.amazon.com/s3/pricing/)

1. Total_download_bandwidth = Amount_of_converted_images_downloaded_from_s3_per_day * (day / 86400s) == (1,000,000 users * 5 MB / file * 5 file / day) * 2.4 * (day / 86400s) * (1GB / 1000MB) ~=  0.69GB / s 

- per monthly basis, 1800 TB is used. Given S3 transfer out pricing is $0.05 per GB, this translates to `$90,000` / month cost


### Number of servers estimation

- AWS EC2 Pricing information can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/)

- Est_number_of_servers_required = Daily_active_users / Server_daily_request_capacity == 1,000,000 / 5,000 = 200 servers

- Given `AWS t4g.medium` costs `$0.0336 server / hour`, it costs
    - `$24.192 server / month`
    - `$4838.40 / month` for 200 servers


### Maximum total costs / month

- The maximum total costs would be `$94,838.40 / month`


## API Design

- Post a convert request

```
postConvertRequest(end_format, image)
```

<table>
    <tbody>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>end_format</td>
            <td>The target format of an image. It's one of: png, webp, jpg</td>
        </tr>
        <tr>
            <td>image</td>
            <td>Image that's being uploaded to server (in blob)</td>
        </tr>
    </tbody>
</table>

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

