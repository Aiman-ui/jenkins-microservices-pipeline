pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
		cleanWs()
                checkout scm
                echo "Code checked out from GitHub"
            }
        }

        stage('Build Docker Images') {
            steps {
                echo "Building Docker images for all services..."
                sh 'docker build -t auth-service ./microservices/auth-service'
                sh 'docker build -t user-service ./microservices/user-service'
                sh 'docker build -t job-service ./microservices/job-service'
            }
        }

        stage('Run Services with Docker Compose') {
            steps {
                echo "Running all services with docker-compose..."
                sh 'docker-compose up -d'
            }
        }
    }
}

