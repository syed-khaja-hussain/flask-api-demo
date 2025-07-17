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
                git branch: 'main', url: 'https://github.com/syed-khaja-hussain/flask-api-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Stop Old Container') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
                    bat "docker stop %CONTAINER_NAME%"
                    bat "docker rm %CONTAINER_NAME%"
                }
            }
        }

        stage('Run New Container') {
            steps {
                bat "docker run -d --name %CONTAINER_NAME% -p %PORT%:5000 %IMAGE_NAME%"
            }
        }
    }
}
