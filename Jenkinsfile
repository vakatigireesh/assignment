pipeline {
    agent any

    stages {
        stage('Get Latest Sourcecode') {
            steps {
	        git 'https://github.com/vakatigireesh/assignment.git'
            }
        }
	    
        stage('Environment preparation') {
            steps {
                echo "-=- preparing project environment -=-"
                // Python dependencies
                sh "pip3 install pandas wheel openpyxl"
            }
        }
        stage('Compile') {
            steps {
                 sh 'python3 parameterCoverage.py'
            }
        }
    }
}
