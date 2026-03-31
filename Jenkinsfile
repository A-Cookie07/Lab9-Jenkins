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

                sh "sudo -l"
                sh 'sudo apt-get -y install python3-ncclient'
                sh 'sudo apt-get -y install python3-pandas'
                sh 'sudo apt-get -y install python3-netaddr'
                sh 'sudo apt-get -y install python3-prettytable'
                sh 'sudo apt-get -y install pylint'
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
    post {
        success {
            script{
                mail(
                to: 'zach0311@comcast.net',
                subject: "Build Success",
                body: "The Jobs all succesfully completed"
                )
            }
        }
    }
}
