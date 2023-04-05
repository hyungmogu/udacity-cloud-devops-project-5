pipeline {
    agent any
    environment {
        AWS_ACCESS_KEY_ID = credentials('aws-access-key-id')
        AWS_SECRET_ACCESS_KEY = credentials('aws-secret-access-key')
        AWS_DEFAULT_REGION = "us-east-1"
        AWS_BACKEND_PUBLIC_KEY_PATH= ""
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
        DOCKER_IMAGE_NAME = "guhyungm7/img-converter"
        CANARY_REPLICAS = 0
    }
    stages {
        stage('Lint') {
            parallel {
                stage('Lint Front-end') {
                    stages {
                        stage("Checkout") {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Pull Hadolint Docker Image") {
                            steps {
                                sh 'docker pull hadolint/hadolint'
                            }
                        }
                        stage("Check Lint") {
                            steps {
                                dir('frontend') {
                                    sh 'docker run --rm -i hadolint/hadolint < Dockerfile'
                                }
                            }
                        }
                    }
                }
                stage('Lint Back-end') {
                    stages {
                        stage("Checkout") {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Pull Hadolint Docker Image") {
                            steps {
                                sh 'docker pull hadolint/hadolint'
                            }
                        }
                        stage("Check Lint") {
                            steps {
                                dir('backend') {
                                    sh 'docker run --rm -i hadolint/hadolint < Dockerfile'
                                }
                            }
                        }
                    }
                }
            }
        }
        stage('Build') {
            parallel {
                stage('Build Front-end') {
                    stages {
                        stage("Checkout") {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Build Docker Image") {
                            steps {
                                dir("frontend") {
                                    sh 'docker build -t guhyungm7/img-converter-frontend:canary -f .'
                                }
                            }
                        }
                        stage("Docker Login") {
                            steps {
                                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                sh 'docker push guhyungm7/img-converter-frontend:canary'
                            }
                        }
                    }
                }
                stage('Build Back-end') {
                    stages {
                        stage('Checkout') {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Build Docker Image") {
                            steps {
                                dir("backend") {
                                    sh 'docker build -t guhyungm7/img-converter:canary -f .'
                                }
                            }
                        }
                        stage("Docker Login") {
                            steps {
                                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                sh 'docker push guhyungm7/img-converter:canary'
                            }
                        }
                    }
                }
            }
        }
        stage('Test & Scan') {
            parallel {
                stage('Test Front-End') {
                    agent {
                        docker {
                            image 'guhyungm7/img-converter-frontend:canary'
                        }
                    }
                    steps {
                        sh 'npm run test:unit'
                    }
                }
                stage('Test Back-End') {
                    agent {
                        docker {
                            image 'guhyungm7/img-converter:canary'
                        }
                    }
                    steps {
                        sh 'python -m unittest discover tests'
                    }
                }
                stage('Scan Front-End') {
                    agent {
                        docker {
                            image 'guhyungm7/img-converter-frontend:canary'
                        }
                    }
                    steps {
                        sh 'npm audit'
                    }
                }
                stage('Scan Back-End') {
                    agent {
                        docker {
                            image 'guhyungm7/img-converter:canary'
                        }
                    }
                    steps {
                        sh 'python -m pip_audit'
                    }
                }
            }
        }
        stage('Build - Production') {
            when {
                branch 'master'
            }
            parallel {
                stage('Build Front-End') {
                    stages {
                        stage("Checkout") {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Build Docker Image") {
                            steps {
                                dir("frontend") {
                                    sh 'docker build -t guhyungm7/img-converter-frontend:latest -f .'
                                }
                            }
                        }
                        stage("Docker Login") {
                            steps {
                                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                sh 'docker push guhyungm7/img-converter-frontend:latest'
                            }
                        }
                    }
                }
                stage('Build Back-End') {
                    stages {
                        stage("Checkout") {
                            steps {
                                checkout scm
                            }
                        }
                        stage("Build Docker Image") {
                            steps {
                                dir("backend") {
                                    sh 'docker build -t guhyungm7/img-converter:latest -f .'
                                }
                            }
                        }
                        stage("Docker Login") {
                            steps {
                                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                sh 'docker push guhyungm7/img-converter:latest'
                            }
                        }
                    }
                }
            }
        }
        stage('Deploy Infrastructure') {
            agent {
                docker {
                    image 'python:3.11-buster'
                }
            }
            when {
                branch 'master'
            }
            stages {
                stage("Checkout") {
                    steps {
                        checkout scm
                    }
                }
                stage("Update Packages") {
                    steps {
                        sh "apt update"
                    }
                }
                stage("Install tar and gzip") {
                    steps {
                        sh "apt-get -y install tar gzip"
                    }
                }
                stage("Install AWS-CLI") {
                    steps {
                        sh "apt-get -y install awscli"
                    }
                }
                stage("Ensure back-end infrastructure exists") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            sh '''
                            aws cloudformation deploy\
                            --template - file.circleci / files / backend.yml\
                                --tags project = udapeople\
                                --stack - name "udapeople-${env.BUILD_ID:0:7}-backend"\
                                --parameter - overrides ID = "${env.BUILD_ID:0:7}"
                            '''

                            instance_id = sh(
                                script: 'aws cloudformation describe-stacks --stack-name "udapeople-${env.BUILD_ID:0:7}-ec2" --query "Stacks[0].Outputs[?OutputKey==`InstanceId`].OutputValue" --output text',
                                returnStdout: true
                            ).trim()

                            os_user = sh(
                                script: 'aws cloudformation describe-stacks --stack-name "udapeople-${env.BUILD_ID:0:7}-ec2" --query "Stacks[0].Outputs[?OutputKey==`DefaultOsUser`].OutputValue" --output text',
                                returnStdout: true
                            ).trim()

                            withEnv(["AWS_BACKEND_STACK_INSTANCE_ID=${instance_id}", "AWS_BACKEND_STACK_OS_USER=${os_user}"]) {
                                echo "AWS_BACKEND_STACK_INSTANCE_ID = ${env.AWS_BACKEND_STACK_INSTANCE_ID}"
                                echo "AWS_BACKEND_STACK_OS_USER = ${env.AWS_BACKEND_STACK_OS_USER}"
                            }
                        }
                        
                    }
                }
                stage("Ensure front-end infrastructure exist") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            sh '''
                            aws cloudformation deploy\
                            --template - file.circleci / files / frontend.yml\
                                --tags project = udapeople\
                                --stack - name "udapeople-${env.BUILD_ID:0:7}-frontend"\
                                --parameter - overrides ID = "${env.BUILD_ID:0:7}"
                            '''
                        }
                    }
                }
                stage("Add back-end ip to ansible inventory") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            sh '''
                            aws ec2 describe-instances \
                            --query 'Reservations[*].Instances[*].PublicIpAddress' \
                            --filters "Name=tag:Name,Values=backend-${env.BUILD_ID:0:7}" \
                            --output text >> .jenkins/ansible/inventory.txt
                            '''
                        }
                    }
                }
            }
        }
        stage('Configure & Install Infrastructure') {
            agent {
                docker {
                    image 'python:3.11-buster'
                }
            }
            when {
                branch 'master'
            }
            stages {
                stage("Checkout") {
                    steps {
                        checkout scm
                    }
                }
                stage("Update Packages") {
                    steps {
                        sh "apt update"
                    }
                }
                stage("Install Ansible") {
                    steps {
                        sh "apt-get -y install ansible"
                    }
                }
                stage("Install AWS-CLI") {
                    steps {
                        sh "apt-get -y install awscli"
                    }
                }
                stage("Add SSH Key to EC2 Instance") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            sh """
                            aws ec2-instance-connect send-ssh-public-key \
                                --instance-id ${env.AWS_BACKEND_STACK_INSTANCE_ID} \
                                --instance-os-user ${env.AWS_BACKEND_STACK_OS_USER} \
                                --ssh-public-key ${env.AWS_BACKEND_PUBLIC_KEY_PATH}
                            """
                        }
                    }
                }
                stage("Run Playbook and Configure server") {
                    steps {
                        dir('.jenkins/ansible') {
                            sh 'ansible-playbook -i inventory.txt configure-server.yml'
                        }
                    }
                }
            }
        }
        stage('Deploy Front-End') {
            agent {
                docker {
                    image 'python:3.11-buster'
                }
            }
            when {
                branch 'master'
            }
            stages {
                stage("Checkout") {
                    steps {
                        checkout scm
                    }
                }
                stage("Update Packages") {
                    steps {
                        sh "apt update"
                    }
                }
                stage("Install tar") {
                    steps {
                        sh "apt-get -y install tar"
                    }
                }
                stage("Install AWS-CLI") {
                    steps {
                        sh "apt-get -y install awscli"
                    }
                }
                stage("Get Backend URL") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            backend_ip = sh(
                                script: 'aws ec2 describe-instances --query 'Reservations[*].Instances[*].PublicIpAddress' --filters "Name=tag:Name,Values=backend-${env.BUILD_ID:0:7}" --output text',
                                returnStdout: true
                            ).trim()

                            withEnv(["AWS_BACKEND_IP=${backend_ip}"]) {
                                echo "AWS_BACKEND_IP = ${env.AWS_BACKEND_IP}"
                            }
                        }
                    }
                }
                stage("Run Playbook and Configure server") {
                    steps {
                        dir('.jenkins/ansible') {
                            sh 'ansible-playbook -i inventory.txt configure-server.yml'
                        }
                    }
                }
            }
        }
        stage('CanaryDeploy') {
            when {
                branch 'master'
            }
            environment {
                CANARY_REPLICAS = 1
            }
            steps {
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'train-schedule-kube-canary.yml',
                    enableConfigSubstitution: true
                )
            }
        }
        stage('DeployToProduction') {
            when {
                branch 'master'
            }
            steps {
                milestone(1)
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'train-schedule-kube.yml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
    post {
        cleanup {
            kubernetesDeploy(
                kubeconfigId: 'kubeconfig',
                configs: 'train-schedule-kube-canary.yml',
                enableConfigSubstitution: true
            )
        }
    }
}