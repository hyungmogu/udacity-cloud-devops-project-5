# Setting Up AWS EC2 Plugin

## Introduction

The AWS EC2 plugin for Jenkins allows you to run your Jenkins jobs on a remote server, such as a separate AWS EC2 instance. This not only provides a performance boost by deploying additional instances whenever necessary, but it also enhances the security of your Jenkins jobs. By leveraging the power of AWS, the plugin enables you to efficiently manage your Jenkins builds and scale your infrastructure to meet your needs.

## Outcome of this Setup Instruction

Ability to launch Jenkin jobs in AWS EC2 instances, and scale when in need.

<img src="https://user-images.githubusercontent.com/6856382/230738833-36fd6c14-5b11-450f-9c2b-aca01b60bcee.png"/>

## Generating IAM for Jenkins

1. From AWS console, click `IAM > Users > Add Users`

<img src="https://user-images.githubusercontent.com/6856382/230739300-e6e8e1fa-ce09-4777-9fce-b4ebc31e8f19.png"/>

2. Fill in `User Name`, click next and select `Attach Policies Directly > AmazonEC2FullAccess`.

<img src="https://user-images.githubusercontent.com/6856382/230739331-794fdaa3-0dcb-4c03-a418-ab84ac11eb4e.png"/>

<img src="https://user-images.githubusercontent.com/6856382/230739344-6c474bd5-65b4-4a91-8733-4786ea79064d.png"/>

3. Select `Next` and complete IAM User Creation

<img src="https://user-images.githubusercontent.com/6856382/230739356-8757663b-a0f2-4683-b959-6ab207331aad.png"/>

4. On IAM main page, select `'created IAM User' > Security Credentials > Create Access Key`

<img src="https://user-images.githubusercontent.com/6856382/230739383-b25e06d6-5483-4236-a6e2-48892b33091f.png"/>

<img src="https://user-images.githubusercontent.com/6856382/230739641-c5910c8d-ccf7-41a1-8482-7624f5d08018.png"/>

<img src="https://user-images.githubusercontent.com/6856382/230739655-49edb320-b490-4ffe-9185-57cd57fdec25.png"/>

5. On Create Access Key page, select `Other` option, and then click `Next`

<img src="https://user-images.githubusercontent.com/6856382/230739843-12c78096-68b2-492f-99d9-5000fb523538.png"/>

6. Finish creating access key by selecting `Create Access Key`

<img src="https://user-images.githubusercontent.com/6856382/230739876-7c3210a9-b43e-406f-b609-69ebefa0b0c6.png" />

7. Copy `Access Key` and `Secret Access Key` and select `Done`

<img src="https://user-images.githubusercontent.com/6856382/230739895-e9d81cb0-55b6-4770-a7cf-6a64c10f2d9e.png"/>

8. On Jenkins page, click `Manage Jenkins > Manage Credentials`

<img src="https://user-images.githubusercontent.com/6856382/230739911-f11ee4ae-7a86-4ffe-92e2-eb8bd4c1869a.png"/>

9. On Manage Credentials page, click `(global) > Add Credentials`

<img src="https://user-images.githubusercontent.com/6856382/230739923-b40cb40e-217d-4da1-b9ec-e85f2b4afdb1.png"/>

<img src="https://user-images.githubusercontent.com/6856382/230739933-453c0e79-0c7a-464e-9ff4-29873a3b0147.png"/>

10. Using AWS IAM credentials copied from step g), fill as follows:
    - Kind: AWS Credentials
    - ID: aws.jenkins.iam.credential (or any other id of choice)
    - Description: AWS Jenkins IAM Credential (or any matching description of choice)
    - Access Key ID: `Access Key` from step g)
    - Secret Access Key: `Secret Access Key` from step g)

11. hit `Create`.

<img src="https://user-images.githubusercontent.com/6856382/230739958-8424e669-308b-48b5-b377-9a5a0ce12f9b.png"/>

## Generating SSH Key Pairs for Jenkins

## Configuring Amazon EC2 Plugin

1. On Jenkins page, click `Manage Jenkins > Manage Nodes and Clouds`

<img src="https://user-images.githubusercontent.com/6856382/230740569-2498c2a1-eadd-4a4a-95d9-617ed575733a.png"/>

2.  Click `Configure Clouds`

<img src="https://user-images.githubusercontent.com/6856382/230740611-e6646c3d-352c-40b4-8527-0ffbe71e8732.png"/>

3. Fill in as follows. The following is what author used to configure EC2 plugin[1]. Sensitive information is omitted.

<img src="https://user-images.githubusercontent.com/6856382/230740665-19959686-89b7-4c32-bc4e-29051df281fd.png"/>


**Full Init Script code**

```
# Install Java
sudo apt-get update
sudo apt install -y default-jdk
sudo apt install -y default-jre
# Install Docker
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -m 0755 -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
# Manage docker as non-root user
# https://www.digitalocean.com/community/questions/how-to-fix-docker-got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket
sudo usermod -aG docker ${USER}
```