pipeline {
    agent any
    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub')
        DOCKER_IMAGE_NAME = "guhyungm7/img-converter:latest"
        CANARY_REPLICAS = 0
    }
    stages {
         stage('Lint Front-end') {
            steps {
                sh 'docker pull hadolint/hadolint'
                sh 'docker run --rm -i hadolint/hadolint < frontend/Dockerfile'
            }
        }
        stage('Lint Back-end') {
            steps {
                sh 'docker pull hadolint/hadolint'
                sh 'docker run --rm -i hadolint/hadolint < backend/Dockerfile'
            }
        }
        stage('Build Front-end') {
            steps {
                dir("frontend") {
                    sh 'docker build -t guhyungm7/img-converter-frontend:canary -f .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push guhyungm7/img-converter-frontend:canary'
                }
            }
        }
        stage('Build Back-end') {
            steps {
                dir("backend") {
                    sh 'docker build -t guhyungm7/img-converter:canary -f .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push guhyungm7/img-converter:canary'
                }
            }
        }
        stage('Test Front-End') {
            agent {
                docker { image 'guhyungm7/img-converter-frontend:canary' }
            }
            steps {
                sh 'npm run test:unit'
            }
        }
        stage('Test Back-End') {
            agent {
                docker { image 'guhyungm7/img-converter:canary' }
            }
            steps {
                sh 'python -m unittest discover tests'
            }
        }
        stage('Scan Front-End') {
             agent {
                docker { image 'guhyungm7/img-converter-frontend:canary' }
            }
            steps {
                sh 'npm audit'
            }
        }
        stage('Scan Back-End') {
            agent {
                docker { image 'guhyungm7/img-converter:canary' }
            }
            steps {
                sh 'python -m pip_audit'
            }
        }
        stage('Deploy Production-Grade Front-End Docker Image') {
            when {
                branch 'master'
            }
            stages {
                stage("Checkout") {
                   steps {
                       checkout scm
                   }
               }
               stage("Build Docker Image") {
                   steps {
                       dir("backend") {
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
        stage('Deploy Production-Grade Back-End Docker Image') {
            when {
                branch 'master'
            }
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
        stage('Deploy Infrastructure') {
            agent {
                docker { image 'python:3.11-buster' }
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
                       sh '''
                       aws cloudformation deploy \
                        --template-file .circleci/files/backend.yml \
                        --tags project=udapeople \
                        --stack-name "udapeople-${env.BUILD_ID:0:7}-backend" \
                        --parameter-overrides ID="${env.BUILD_ID:0:7}"
                       '''
                   }
               }
               stage("Ensure front-end infrastructure exist") {
                   steps {
                       sh '''
                       aws cloudformation deploy \
                        --template-file .circleci/files/frontend.yml \
                        --tags project=udapeople \
                        --stack-name "udapeople-${env.BUILD_ID:0:7}-frontend" \
                        --parameter-overrides ID="${env.BUILD_ID:0:7}"
                       '''
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