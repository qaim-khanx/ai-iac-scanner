pipeline {
    agent any
    environment {
        // You will set this in Jenkins Credentials (Secret Text)
        GOOGLE_API_KEY = credentials('GOOGLE_API_KEY')
    }
    stages {
        stage('Security Scan') {
            steps {
                echo 'Running AI Security Scan...'
                // Using the venv python to ensure dependencies are loaded
                sh 'venv/bin/python3 scanner.py'
            }
        }
        stage('Terraform Plan') {
            steps {
                echo 'Running Terraform Plan...'
                sh 'terraform init'
                sh 'terraform plan'
            }
        }
    }
}
