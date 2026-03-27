pipeline {
    agent any

    environment {
        VAR1 = 'string'
    }

    stages {
        stage('Pre-OP testing') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                echo "Multiline steps work too"
                chmod 700 basicpython.py
                ls -la
                '''
                sh "echo variable is ${VAR1}"
            }
        }

        stage('Package Management'){
            steps {
                sh 'apt-get install python3-ncclient'
                sh 'apt-get install python3-pandas'
                sh 'apt-get install python3-netaddr'
                sh 'apt-get install python3-prettytable'
            }
        }
    }
}
