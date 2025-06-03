pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo "Assuming code is already on local machine"
            }
        }

        stage('Build Docker Images') {
            steps {
                dir('Lab') {
                    echo "Building Docker images for all services..."
                    sh 'docker build -t auth-service ./microservices/auth-service'
                    sh 'docker build -t user-service ./microservices/user-service'
                    sh 'docker build -t job-service ./microservices/job-service'
                }
            }
        }

        stage('Run Services with Docker Compose') {
            steps {
                dir('Lab') {
                    echo "Running all services using docker-compose..."
                    sh 'docker-compose up -d'
                }
            }
        }
    }
}

