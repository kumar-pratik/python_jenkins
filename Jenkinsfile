pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "cd src"
                sh "python add_val.py 32 bit"
                sh "cd .."
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