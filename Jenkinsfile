pipeline {
    agent any

    stages {
        stage('Get Latest Sourcecode') {
            steps {
	        git 'https://github.com/vakatigireesh/assignment.git'
            }
        }
        stage('Compile') {
            steps {
                 sh 'python3 parameterCoverage.py'
            }
        }
    }
}
