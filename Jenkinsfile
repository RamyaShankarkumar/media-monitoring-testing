pipeline {
    agent any

    environment {
        SLACK_WEBHOOK_URL = credentials('SLACK_WEBHOOK_URL')
    }

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
                echo 'CHECKING FOR GITHUB WEBHOOK'
                echo 'CHECKING FOR SLACK WEBHOOK'
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
            sh """
            curl -X POST -H 'Content-type: application/json' --data '{"text":"Build SUCCESS : $JOB_NAME #$BUILD_NUMBER\"}' $SLACK_WEBHOOK_URL
            """
            //slackSend channel: '#webhook-test', message: "Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
        failure {
            sh """
            curl -X POST -H 'Content-type: application/json' --data '{"text":"Build FAILED : $JOB_NAME #$BUILD_NUMBER\"}' $SLACK_WEBHOOK_URL
            """
            //slackSend channel: '#webhook-test', message: "Build FAILED: ${env.JOB_NAME} #${env.BUILD_NUMBER}"
        }
    }
}
