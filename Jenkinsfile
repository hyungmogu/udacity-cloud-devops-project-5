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
            steps {
                dir("frontend") {
                    sh 'docker build -t guhyungm7/img-converter-frontend:latest -f .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push guhyungm7/img-converter-frontend:latest'
                }
            }
        }
        stage('Deploy Production-Grade Back-End Docker Image') {
            agent {
                docker { image 'guhyungm7/img-converter:canary' }
            }
            when {
                branch 'master'
            }
            steps {
                dir("backend") {
                    sh 'docker build -t guhyungm7/img-converter:latest -f .'
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    sh 'docker push guhyungm7/img-converter:latest'
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