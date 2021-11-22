node {
    stage('git checkout') {
        git credentialsId: 'bms-git-credentials', url: 'https://github.com/mokshkhajanchi/book-my-show.git', branch: 'main'
    }
    stage('build docker image') {
        sh 'docker build -t mokshkhajanchi/book-my-show-django-api:1.0 .'
    }
}