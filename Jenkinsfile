pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "guhyungm7/img-type-converter"
        CANARY_REPLICAS = 0
    }
    stages {
        stage('Build Front-End') {
            agent {
                docker {
                    image: "node:lts-alpine"
                }
            }
            steps {
               
            }
        }
         stage('Lint') {
            when {
                branch 'master'
            }
            steps {

            }
        }
        stage('Test Front-End') {
            when {
                branch 'master'
            }
            steps {

            }
        }
        stage('Test Back-End') {
            when {
                branch 'master'
            }
            steps {

            }
        }
        stage('Scan Front-End') {
            when {
                branch 'master'
            }
            steps {

            }
        }
        stage('Scan Back-End') {
            when {
                branch 'master'
            }
            steps {

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