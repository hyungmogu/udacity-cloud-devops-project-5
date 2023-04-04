pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "guhyungm7/img-converter:latest"
        CANARY_REPLICAS = 0
    }
    stages {
        stage('Build Front-end') {
            agent {
                docker {
                    image: 'node:18-buster'
                }
            }
            steps {
                echo 'Building Front-end'
            }
        }
        stage('Build Back-end') {
            agent {
                docker {
                    image: 'php:7.4-fpm'
                }
            }
            steps {
                echo 'Building Laravel and Back-end'
            }
        }
         stage('Lint Front-end') {
            steps {
                cd 
                echo 'Linting Front-end'
            }
        }
        stage('Lint Back-end') {
            steps {
                echo 'Linting Back-end'
            }
        }
        stage('Test Front-End') {
            agent {
                docker {
                    image: 'guhyungm7/img-converter-frontend:canary'
                }
            }
            when {
                branch 'master'
            }
            steps {
                docker.image('guhyungm7/img-converter-frontend:canary').inside {
                    sh 'npm run test:unit'
                }
            }
        }
        stage('Test Back-End') {
            agent {
                docker {
                    image: 'guhyungm7/img-converter:canary'
                }
            }
            when {
                branch 'master'
            }
            steps {
                docker.image('guhyungm7/img-converter:canary').inside {
                    sh 'python -m unittest discover tests'
                }
            }
        }
        stage('Scan Front-End') {
            agent {
                docker {
                    image: 'guhyungm7/img-converter-frontend:canary'
                }
            }
            when {
                branch 'master'
            }
            steps {
                docker.image('guhyungm7/img-converter-frontend:canary').inside {
                    sh 'npm audit'
                }
            }
        }
        stage('Scan Back-End') {
            agent {
                docker {
                    image: 'guhyungm7/img-converter:canary'
                }
            }
            when {
                branch 'master'
            }
            steps {
                docker.image('guhyungm7/img-converter:canary').inside {
                    sh 'python -m pip_audit'
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker_hub_login') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
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