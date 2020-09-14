pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "python src/add_val.py 32 bit"
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh "python test.py"
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}