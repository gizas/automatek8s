pipeline {
    agent any
    stages {
        stage('Build') {
            steps {

                withCredentials([usernamePassword(credentialsId: 'elastic', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                // available as an env variable, but will be masked if you try to print it out any which way
                // note: single quotes prevent Groovy interpolation; expansion is by Bourne Shell, which is what you want
                sh 'echo $PASSWORD'
                // also available as a Groovy variable
                echo USERNAME
                // or inside double quotes for string interpolation
                echo "username is $USERNAME"
                sh 'python3 --version'
                sh 'python3 kibana_api.py -apikey $PASSWORD'
                }
            }
        }
    }
}