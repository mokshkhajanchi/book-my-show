pipeline {
    agent any
    stages{
        stage("git clone") {
            steps {
                git branch: 'main',
                git credentialsId: 'bms-git-credentials',
                url: 'https://github.com/mokshkhajanchi/book-my-show.git'
            }
        }
        stage("build") {
            steps {
                sh 'docker build -t mokshkhajanchi/book-my-show-django-api:1.0 .'
            }
        }
        stage("deploy") {
            steps {
                withCredentials([string(credentialsId: 'bms-docker-credentials', variable: 'bms-docker-credentials')]) {
                    sh "docker login -u mokshkhajanchi -p ${bms-docker-credentials}"
                }
                sh 'docker push mokshkhajanchi/book-my-show-django-api:1.0'
            }
        }
    }
    post {
		always {
			sh 'docker logout'
		}
	}
}