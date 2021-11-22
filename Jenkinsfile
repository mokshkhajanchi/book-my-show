node {
    environment {
        bms_docker_credentials = credentials('bms-docker-credentials')
    }
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    stage('git checkout') {
        git credentialsId: 'bms-git-credentials', url: 'https://github.com/mokshkhajanchi/book-my-show.git', branch: 'main'
    }
    // stage('build docker image') {
    //     sh 'docker build -t mokshkhajanchi/book-my-show-django-api:1.0 .'
    // }
    stage('push docker image') {
        sh "echo ${bms_docker_credentials}"
        // sh "docker login -u mokshkhajanchi -p ${bmsdockercredentials}"
        // sh 'docker push mokshkhajanchi/book-my-show-django-api:1.0'
    }
    // post {
	// 	always {
	// 		sh 'docker logout'
	// 	}
	// }
}