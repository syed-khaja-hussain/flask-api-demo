pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-api-jenkins"
        CONTAINER_NAME = "flask-api-jenkins"
        PORT = "5000"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/syed-khaja-hussain/flask-api-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    bat "docker build -t %IMAGE_NAME% ."
                }
            }
        }

        stage('Stop Old Container') {
            steps {
                script {
                    bat "docker stop %CONTAINER_NAME% || echo not running"
                    bat "docker rm %CONTAINER_NAME% || echo not running"
                }
            }
        }

        stage('Run New Container') {
            steps {
                script {
                    bat "docker run -d --name %CONTAINER_NAME% -p %PORT%:5000 %IMAGE_NAME%"
                }
            }
        }
    }
}
