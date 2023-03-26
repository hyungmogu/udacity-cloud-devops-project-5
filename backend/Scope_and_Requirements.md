# Scope and Requirements

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
1. (1,000,000 users / day * 5 MB / file * 5 files a day) * (1 + 2.4) = 85 million MB = 85 TB / day

2. 85 TB / day ~= 59.027GB / minutes ~= 885 GB / 15 minutes

- Given the constraints, the amount of storage required is 885 GB.

- In AWS's S3, this roughly translates to $20 USD / month