# Installing Jenkins

This installation assumes that user is using Debian/Ubuntu as operating system. More installation instruction can be found [here](https://www.jenkins.io/doc/book/installing/linux/#debianubuntu).

## Pre-requisites

Jenkins requires that the running operating system has following minimum hardware requirements:

- 256 MB of RAM
- 1 GB of drive space (although 10 GB is a recommended minimum if running Jenkins as a Docker container)

## Installing Jenkins Core (Long Term Release)

In Debian/Ubuntu terminal, type the following:

```
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

## Installation of Java

In Debian/Ubuntu terminal, after installing Jenkins core, type the following:

```
sudo apt update
sudo apt install openjdk-11-jre
```

## References

1. Jenkins Community of Developers. (2023, April 8th). Installing Jenkins, Linux. Jenkins. https://www.jenkins.io/doc/book/installing/linux/#debianubuntu