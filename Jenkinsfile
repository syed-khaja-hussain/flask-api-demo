pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-api-jenkins"
    }

    stages {
       stage('Clone') {
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
                bat "docker stop %IMAGE_NAME% || echo not running"
                bat "docker rm %IMAGE_NAME% || echo not running"
            }
        }

        stage('Run New Container') {
            steps {
                bat "docker run -d --name %IMAGE_NAME% -p 5000:5000 %IMAGE_NAME%"
            }
        }
    }
}
