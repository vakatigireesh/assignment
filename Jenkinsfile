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
                sh "pip install pandas wheel openpyxl"
            }
        }
        stage('Compile') {
            steps {
                 sh 'python parametercoverage.py'
            }
        }
        stage('Test') {
            steps {
		input message: 'Are you sure to proceed to next step? ', ok: 'Yes'
              
            }
        }
    }
}
