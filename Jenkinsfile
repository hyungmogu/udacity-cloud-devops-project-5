def checkoutCode() {
  stage("Checkout") {
    steps {
      def commit = checkout scm
      echo "Latest commit ID: ${commit.GIT_COMMIT}"
    }
  }
}

def updatePackages() {
    stage("Update Packages") {
        steps {
            sh "apt update"
        }
    }
}

def installPackage(packageName) {
    stage("Install ${packageName}") {
        steps {
            sh "apt-get -y install ${packageName}"
        }
    }
}

// ===== Linting =======

def pullHadolintImage() {
    stage("Pull Hadolint Docker Image") {
        steps {
            script {
                docker.image('hadolint/hadolint').pull()
            }
        }
    }
}
def lintDockerfile(dirName) {
    stage("Lint ${dirName}") {
        steps {
            script {
                docker.withTool('hadolint') {
                    dir(dirName) {
                        sh 'hadolint < Dockerfile'
                    }
                }
            }
        }
    }
}

pipeline {
    agent any
    environment {
        PUBLIC_KEY_PATH= "${env.PUBLIC_KEY_PATH}"
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
        DOCKER_IMAGE = "${env.DOCKER_USER_ID}/img-converter"
    }
    stages {
        stage('Lint') {
            parallel {
                stage('Lint Front-end') {
                    stages {
                        checkoutCode()
                        pullHadolintImage()
                        lintDockerfile('frontend')
                    }
                }
                stage('Lint Back-end') {
                    stages {
                        checkoutCode()
                        pullHadolintImage()
                        lintDockerfile('backend')
                    }
                }
            }
        }
        stage('Build') {
            def dockerImageFrontEnd
            def dockerImageBackEnd
            parallel {
                stage('Build Front-end') {
                    stages {
                        checkoutCode()
                        stage("Build Docker Image") {
                            steps {
                                script {
                                    dockerImageFrontEnd = docker.build("${env.DOCKER_IMAGE}-frontend", "frontend")
                                }
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                script {
                                    withCredentials([
                                        usernamePassword(credentialsId: 'docker-hub-key', passwordVariable: 'DOCKERHUB_PW', usernameVariable: 'DOCKERHUB_USERNAME')
                                    ]) {
                                        docker.withRegistry('', 'docker-hub-key') {
                                            dockerImageFrontEnd.push("${env.BUILD_NUMBER}-canary")
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                stage('Build Back-end') {
                    stages {
                        checkoutCode()
                        stage("Build Docker Image") {
                            steps {
                                script {
                                    dockerImageBackEnd = docker.build("${env.DOCKER_IMAGE}", "backend")
                                }
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                script {
                                    withCredentials([
                                        usernamePassword(credentialsId: 'docker-hub-key', passwordVariable: 'DOCKERHUB_PW', usernameVariable: 'DOCKERHUB_USERNAME')
                                    ]) {
                                        docker.withRegistry('', 'docker-hub-key') {
                                            dockerImageBackEnd.push("${env.BUILD_NUMBER}-canary")
                                        }
                                    }
                                }
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
                            image "${env.DOCKER_IMAGE}-frontend:${env.BUILD_NUMBER}-canary"
                        }
                    }
                    steps {
                        sh 'npm run test:unit'
                    }
                }
                stage('Test Back-End') {
                    agent {
                        docker {
                            image "${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}-canary"
                        }
                    }
                    steps {
                        sh 'python -m unittest discover tests'
                    }
                }
                stage('Scan Front-End') {
                    agent {
                        docker {
                            image "${env.DOCKER_IMAGE}-frontend:${env.BUILD_NUMBER}-canary"
                        }
                    }
                    steps {
                        sh 'npm audit'
                    }
                }
                stage('Scan Back-End') {
                    agent {
                        docker {
                            image "${env.DOCKER_IMAGE}:${env.BUILD_NUMBER}-canary"
                        }
                    }
                    steps {
                        sh 'python -m pip_audit'
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
                checkoutCode()
                updatePackages()
                installPackage("tar")
                installPackage("gzip")
                installPackage("ansible")
                installPackage("awscli")
                stage("Ensure back-end infrastructure exists") {
                    steps {
                        withCredentials([[
                            $class: 'AmazonWebServicesCredentialsBinding',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY',
                            region: 'AWS_DEFAULT_REGION'
                        ]]) {
                            def tagName = 'project'
                            def tagValue = 'img-converter-backend'

                            // Execute the AWS CLI command and parse the output
                            def awsResponse = sh(returnStdout: true, script: "aws cloudformation list-stacks --query 'StackSummaries[?contains(Tags[?Key==\`$tagName\`].Value, \`$tagValue\`)].StackName' --output json").trim()
                            def stackList = readJSON text: awsResponse

                            if (stackList.size() > 0) {
                                echo "Stack with tag $tagName = $tagValue already exists. Skipping backend stack creation."
                            } else {
                                echo "Stack with tag $tagName = $tagValue doesn't exists. Continuing stack creation."
                                
                                sh '''
                                aws cloudformation deploy\
                                --template - file.circleci / files / backend.yml\
                                    --tags project = img-converter-backend\
                                    --stack - name "img-converter-${env.BUILD_ID:0:7}-backend"\
                                    --parameter - overrides ID = "${env.BUILD_ID:0:7}"
                                '''

                                instance_id = sh(
                                    script: 'aws cloudformation describe-stacks --stack-name "img-converter-${env.BUILD_ID:0:7}-ec2" --query "Stacks[0].Outputs[?OutputKey==`InstanceId`].OutputValue" --output text',
                                    returnStdout: true
                                ).trim()

                                os_user = sh(
                                    script: 'aws cloudformation describe-stacks --stack-name "img-converter-${env.BUILD_ID:0:7}-ec2" --query "Stacks[0].Outputs[?OutputKey==`DefaultOsUser`].OutputValue" --output text',
                                    returnStdout: true
                                ).trim()

                                withEnv(["AWS_BACKEND_STACK_INSTANCE_ID=${instance_id}", "AWS_BACKEND_STACK_OS_USER=${os_user}"]) {
                                    echo "AWS_BACKEND_STACK_INSTANCE_ID = ${env.AWS_BACKEND_STACK_INSTANCE_ID}"
                                    echo "AWS_BACKEND_STACK_OS_USER = ${env.AWS_BACKEND_STACK_OS_USER}"
                                }
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
                            def tagName = 'project'
                            def tagValue = 'img-converter-frontend'

                            // Execute the AWS CLI command and parse the output
                            def awsResponse = sh(returnStdout: true, script: "aws cloudformation list-stacks --query 'StackSummaries[?contains(Tags[?Key==\`$tagName\`].Value, \`$tagValue\`)].StackName' --output json").trim()
                            def stackList = readJSON text: awsResponse

                            if (stackList.size() > 0) {
                                echo "Stack with tag $tagName = $tagValue already exists. Skipping backend stack creation."
                            } else {
                                echo "Stack with tag $tagName = $tagValue doesn't exists. Continuing stack creation."

                                sh '''
                                aws cloudformation deploy\
                                --template - file.circleci / files / frontend.yml\
                                    --tags project = img-converter-frontend\
                                    --stack - name "img-converter-${env.BUILD_ID:0:7}-frontend"\
                                    --parameter - overrides ID = "${env.BUILD_ID:0:7}"
                                '''
                            }
                        }
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
                                --ssh-public-key ${env.PUBLIC_KEY_PATH}
                            """
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
                stage("Run Playbook and Configure server") {
                    steps {
                        dir('.jenkins/ansible') {
                            sh 'ansible-playbook -i inventory.txt configure-server.yml'
                        }
                    }
                }
            }
        }
        stage('Deploy') {
            parallel {
                stage('Deploy Front-End') {
                    def dockerImageFrontEnd
                    agent {
                        docker {
                            image 'python:3.11-buster'
                        }
                    }
                    when {
                        branch 'master'
                    }
                    stages {
                        checkoutCode()
                        updatePackages()
                        installPackage("tar")
                        installPackage("awscli")
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
                        stage("Build Docker Image") {
                            steps {
                                script {
                                    dockerImageFrontEnd = docker.build("${env.DOCKER_IMAGE}-frontend", "frontend")
                                }
                            }
                        }
                        stage("Run Build") {
                            steps {
                                script {
                                    dockerImageFrontEnd.withRun('-e BACKEND_IP=${env.AWS_BACKEND_IP} -v $(pwd)/dist:/app/dist') {
                                        echo "========== BUILD RESULTS ==========="
                                        dir("frontend") {
                                            sh 'ls dist'
                                        }        
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
                stage('Deploy Back-End') {
                    agent {
                        docker {
                            image 'python:3.11-buster'
                        }
                    }
                    when {
                        branch 'master'
                    }
                    stages {
                        checkoutCode()
                        updatePackages()
                        installPackage("tar")
                        installPackage("ansible")
                        stage("Build Docker Image") {
                            steps {
                                script {
                                    dockerImageBackEnd = docker.build("${env.DOCKER_IMAGE}", "backend")
                                }
                            }
                        }
                        stage("Push to Docker Hub") {
                            steps {
                                script {
                                    withCredentials([
                                        usernamePassword(credentialsId: 'docker-hub-key', passwordVariable: 'DOCKERHUB_PW', usernameVariable: 'DOCKERHUB_USERNAME')
                                    ]) {
                                        docker.withRegistry('', 'docker-hub-key') {
                                            dockerImageBackEnd.push("${env.BUILD_NUMBER}-latest")
                                        }
                                    }
                                }
                            }
                        }
                        stage("Run Playbook and Apply New Image to Server") {
                            steps {
                                dir('.jenkins/ansible') {
                                    sh 'ansible-playbook -i inventory.txt deploy-backend.yml'
                                }
                            }
                        }
                    }
                }
            }
        }
        stage('Smoke Test') {
            agent {
                docker {
                    image 'python:3.11-buster'
                }
            }
            when {
                branch 'master'
            }
            stages {
                checkoutCode()
                updatePackages()
                installPackage("curl")
                installPackage("awscli")
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
                parallel {
                    stage("Backend smoke test") {
                        steps {
                            sh '''
                            if curl "${env.AWS_BACKEND_IP}/api/status" | grep "ok"
                            then
                                exit 0
                            else
                                exit 1
                            fi
                            '''
                        }
                    }
                    stage("Frontend smoke test") {
                        steps {
                            sh '''
                            URL="http://img-converter-${env.BUILD_ID:0:7}.s3-website-us-east-1.amazonaws.com/"            
                            echo ${URL} 
                            if curl -s ${URL} | grep "Convert"
                            then
                                exit 0
                            else
                                exit 1
                            fi

                            '''
                        }
                    }
                }
            }
        }
    }
}