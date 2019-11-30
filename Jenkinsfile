pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/Users/gog/Documents/GitHub/AgileAssessment2/HelloPython.py sources/calc.py'
            }
        }
    }
}