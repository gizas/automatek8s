pipeline {
    agent any
    stages {
        stage('Verify Version') {
            steps {
                sh 'python3 —version'
            }
        }
        stage('Test') { 
            steps {
                sh 'python3 kibana_api.py -apikey M18weTlJSUJqcHYwQ1FaV0pKMVM6VjlfZlZzd0lTb2VJN21faXIxQ1FoZw=='
            }

        }
    }
}