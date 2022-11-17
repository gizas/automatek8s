pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'elastic', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                    sh 'python3 --version'
                    //sh 'python3 kibana_api.py -apikey $PASSWORD -url https://elastic-package-stack_kibana_1:5601 -k 1.26.0'
                    output = sh(script: 'python3 kibana_api.py -apikey $PASSWORD -url https://elastic-package-stack_kibana_1:5601 -v 1.27.1',returnStdout: true).trim()
                    echo output
                    }
                }
            }    
        }
        stage ('Starting Agent Installation') {
            steps{
            build job: 'Install Managed Agent', parameters: [[$class: 'StringParameterValue', name: 'TOKENID', value: output]]
            }
        }
    }


}