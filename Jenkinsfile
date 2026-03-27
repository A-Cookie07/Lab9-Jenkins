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
                sh 'sudo apt-get update'
                sh 'sudo apt-get -y install python3-ncclient'
                sh 'sudo apt-get -y install python3-pandas'
                sh 'sudo apt-get -y install python3-netaddr'
                sh 'sudo apt-get -y install python3-prettytable'
            }
        }
    }
}
