pipeline {
    agent any
    environment {
        GOOGLE_API_KEY = credentials('GOOGLE_API_KEY')
    }
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Creating Virtual Environment...'
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install google-genai'
            }
        }
        stage('Security Scan') {
            steps {
                echo 'Running AI Security Scan...'
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
