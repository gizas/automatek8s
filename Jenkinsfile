pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'elastic', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                script {
                    sh 'python3 --version'
                    sh 'python3 kibana_api.py -apikey $PASSWORD -url https://elastic-package-stack_kibana_1:5601 -k 1.26.0'
                }
                def fleet_token = readFile "${env.WORKSPACE}/finish.txt"
                echo $fleet_token
                }
            }
        }
    }
}