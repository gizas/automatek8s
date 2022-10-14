pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python3 --version'
                sh 'python3 kibana_api.py -apikey M18weTlJSUJqcHYwQ1FaV0pKMVM6VjlfZlZzd0lTb2VJN21faXIxQ1FoZw=='
            }
        }
    }
}