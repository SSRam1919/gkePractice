pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'rthatikonda/text-generator-app'
        DOCKER_HUB_CREDENTIALS = 'docker-hub-credentials'
        KUBE_CONFIG_CREDENTIALS = 'kube-config' // Ensure this matches the ID used in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-repo/text-generator-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${env.DOCKER_HUB_REPO}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', "${DOCKER_HUB_CREDENTIALS}") {
                        dockerImage.push()
                        dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                withCredentials([file(credentialsId: "${KUBE_CONFIG_CREDENTIALS}", variable: 'KUBECONFIG')]) {
                    sh 'kubectl apply -f k8s/pod.yaml --kubeconfig=$KUBECONFIG'
                    sh 'kubectl apply -f k8s/service.yaml --kubeconfig=$KUBECONFIG'
                }
            }
        }
    }
}

