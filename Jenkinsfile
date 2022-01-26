pipeline {
    agent none
    stages {
        stage('Build') {
            agent any {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile parametercoverage.py'
            }
        }
    }
}
