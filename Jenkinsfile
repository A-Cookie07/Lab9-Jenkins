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
                sh 'apt-get update'
                sh 'apt-get -y install python3-ncclient'
                sh 'apt-get -y install python3-pandas'
                sh 'apt-get -y install python3-netaddr'
                sh 'apt-get -y install python3-prettytable'
                sh 'apt-get -y install pylint'
            }
        }

        stage('Python Syntax'){
            steps{
                sh 'pylint --fail-under=5 ./netman_netconf_obj2.py'
            }
        }

        stage('Run the Application'){
            steps{
                sh 'python3 ./netman_netconf_obj2.py'
            }
        }

        stage('Test Results of Application'){
            steps{
                sh 'python3 test_suite.py'
            }
        }


    }
}
