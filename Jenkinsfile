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
                 sh '''pip install pandas
		    pip install wheel
			    pip install pyxl
		    python parametercoverage.py'''
            }
        }
        stage('Test') {
            steps {
		input message: 'Are you sure to proceed to next step? ', ok: 'Yes'
              
            }
        }
    }
}
