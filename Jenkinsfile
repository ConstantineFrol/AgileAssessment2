Jenkinsfile (Declarative Pipeline)
pipeline {
    agent { none { image 'python:3.5.1' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
    }
}