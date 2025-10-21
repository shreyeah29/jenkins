pipeline {
    agent any

    environment {
        // Change this to your Docker Hub username
        DOCKERHUB_USER = 'shreyeah29'
        IMAGE_NAME = 'myapp'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo '📦 Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                script {
                    sh 'docker build -t ${DOCKERHUB_USER}/${IMAGE_NAME}:latest -f app/Dockerfile ./app'

                }
            }
        }

        stage('Run Container (Test)') {
    steps {
        echo '🚀 Running container to verify build...'
        script {
            sh '''
            docker stop temp-${IMAGE_NAME} || true
            docker rm temp-${IMAGE_NAME} || true
            docker run -d -p 5005:5001 --name temp-${IMAGE_NAME} ${DOCKERHUB_USER}/${IMAGE_NAME}:latest
            sleep 5
            docker ps
            docker stop temp-${IMAGE_NAME}
            docker rm temp-${IMAGE_NAME}
            '''
        }
    }
}

        stage('Push to Docker Hub') {
            steps {
                echo '📤 Pushing image to Docker Hub...'
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh '''
                    echo $PASSWORD | docker login -u $USERNAME --password-stdin
                    docker push ${DOCKERHUB_USER}/${IMAGE_NAME}:latest
                    docker logout
                    '''
                }
            }
        }
    }

    post {
        success {
            echo '✅ Build and push successful!'
        }
        failure {
            echo '❌ Build failed. Please check the logs.'
        }
    }
}
