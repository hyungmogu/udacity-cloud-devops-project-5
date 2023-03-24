pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = "guhyungm7/img-type-converter"
        CANARY_REPLICAS = 0
    }
    stages {
        stage('Build') {
            steps {
                echo 'Running build automation'
                sh './gradlew build --no-daemon'
                archiveArtifacts artifacts: 'dist/img-type-converter-frontend.zip'
                archiveArtifacts artifacts: 'dist/img-type-converter-backend.zip'
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