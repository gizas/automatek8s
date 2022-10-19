// Define variable
def FLEET_TOKEN

pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'elastic', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                script {
                    sh 'python3 --version'
                    sh 'python3 kibana_api.py -apikey $PASSWORD -url https://elastic-package-stack_kibana_1:5601 -k 1.26.0'
                    FLEET_TOKEN = sh(script: 'cat finish.txt', returnStdout: true).trim()
                    echo $FLEET_TOKEN
                }
                }
            }
        }
    }
}