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
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop Old Container') {
            steps {
                sh "docker stop $IMAGE_NAME || true"
                sh "docker rm $IMAGE_NAME || true"
            }
        }

        stage('Run New Container') {
            steps {
                sh "docker run -d --name $IMAGE_NAME -p 5000:5000 $IMAGE_NAME"
            }
        }
    }
}
