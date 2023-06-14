pipeline {
    agent any
    stages {
        stage('Transform Yaml to Json') {
            steps {
                script {
                sh 'python3 --version'
                filestransfomred = sh(script: 'python3 converter_yaml_json.py',returnStdout: true).trim()
                echo filestransfomred
                }
            }    
        }
        stage('Build') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'elastic', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    script {
                    output = sh(script: 'python3 kibana_api.py -apikey $PASSWORD -url https://elastic-package-stack_kibana_1:5601 -v 1.42.0',returnStdout: true).trim()
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
