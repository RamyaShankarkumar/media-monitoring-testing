pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out successfully'
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                  python3 --version
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }
        
        stage('Build') {
            steps {
                echo 'Build stage running'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Test stage running'
                sh '''
                  . venv/bin/activate
                  pytest api-tests/ -m "not integration" --html=reports/report.html --self-contained-html
                '''
                echo 'CHECKING FOR POLLING'
                echo 'CHECKING FOR WEBHOOK'
            }
        }

        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.html', allowEmptyArchive: false
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploy stage (dummy)'
            }
        }
    }

    post {
        success {
            slackSend channel: '#ci-notifications', message: "Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
        failure {
            slackSend channel: '#ci-notifications', message: "Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
