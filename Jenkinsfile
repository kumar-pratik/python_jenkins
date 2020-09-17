pipeline {
    agent {label 'Linux'}

    stages {
        stage('Source') {
            steps {
                git 'https://github.com/kumar-pratik/python_jenkins.git'
            }
        }
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