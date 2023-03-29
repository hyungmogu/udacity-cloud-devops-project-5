# Capstone Project for Cloud DevOps Engineer Nanodegree

This is capstone project for Udacity's Cloud DevOps Engineer Nanodegree. 

## Scope of the project

- Jenkins will be used for CI and CD
- Rolling Deployment will be used
- Cloudformation will be used to build infastructure
- Kubernetes cluster will be built from scratch on AWS
- Kubernetes cluster will be initialized using Ansible and Cloudformation

## Pre-Requisites

## Installation

## Pipeline, Architecture and System Design

<img src="https://user-images.githubusercontent.com/6856382/219821091-e647fe37-0c6f-40ec-a483-2ee99b91ae1d.png"/>

### Deployment Architecture

<img src="https://user-images.githubusercontent.com/6856382/226086046-10f2ec21-c2fb-418d-aa1b-48557938969d.jpeg">

### Infrastructure Diagram

<img src="https://user-images.githubusercontent.com/6856382/228256905-15daa4fd-9fd8-4d83-9e6a-55415689c22a.jpeg"/> 

### Kubernetes Cluster Diagram

<img src="https://user-images.githubusercontent.com/6856382/228103460-aa26c2a0-324a-4515-9112-b2f02f675b24.jpeg"/>

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
    4. Image storage for conversion 

3. Performance: The conversion should be done as quick as possible, as additional delays will clog the system.

#### Resource Estimation
1. Estimated number of daily active users: 1 million (for demonstration purposes)
2. Max file size per image: 5MB (1280 x 960, png)
3. Max number of files submitted per user: 5
4. Max number of times a user could use this service a day: 5
5. Max size of an image after conversion: 12MB (From 5MB, jpg -> png)

#### Resource Estimation Constratints

1. Max time of withholding image data on storage: 15 minutes

#### Storage Estimation
1. (1,000,000 users * 5 MB / file * 5 file / day) * (1 + 2.4) = 85 million MB = 85 TB / day

2. 85 TB / day ~= 59.027GB / minutes ~= 885 GB / 15 minutes

- Given the constraints, the amount of storage required is 885 GB.

- In AWS's S3, this roughly translates to $20 USD / month

#### Bandwidth Estimation

- `upload:download` ratio is assumed to be 1 (meaning, for every upload, there is equivalent number of downloads)

##### The bandwidth required for uploading videos

1. Total_bandwidth == Amount_of_files_uploaded_to_server_per_day * (day / 86400s) ==  1,000,000 user * 5 MB / file * 5 file / day ~= 0.28GB Gbps


```
(1,000,000 users / day * 5 MB / file * 5 file / day) * (1GB / 1000MB) * (day / 86400s) ~= 0.28GB / s
```

##### The bandwidth required for downloading videos

- More info: [here](https://aws.amazon.com/s3/pricing/)

1. Total_download_bandwidth = Amount_of_converted_images_downloaded_from_s3_per_day * (day / 86400s) == (1,000,000 users * 5 MB / file * 5 file / day) * 2.4 * (day / 86400s) * (1GB / 1000MB) ~=  0.69GB / s 

- per monthly basis, 1800 TB is used. Given S3 transfer out pricing is $0.05 per GB, this translates to `$90,000` / month cost


#### Number of servers estimation

- AWS EC2 Pricing information can be found [here](https://aws.amazon.com/ec2/pricing/on-demand/)

- Est_number_of_servers_required = Daily_active_users / Server_daily_request_capacity == 1,000,000 / 5,000 = 200 servers

- Given `AWS t4g.medium` costs `$0.0336 server / hour`, it costs
    - `$24.192 server / month`
    - `$4838.40 / month` for 200 servers


#### Maximum total costs / month

- The maximum total costs would be `$94,838.40 / month`


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

## Testing

#