pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                echo "Multiline steps work too"
                sudo chmod 700 basicpython.py
                ls -la
                '''
            }
        }
    }
}
