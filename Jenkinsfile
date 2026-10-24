pipeline
{
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                echo "Build Docker Image"
                bat "docker build -t digitalvisitorapp:v1 ."
            }
        }
        stage('Docker Login'){
            steps{
                bat 'docker login -u supriyamallesh -p Supriya@206' 
            }
        }
        stage('push Docker Image to Docker Hub'){
            steps{
                echo "push Docker Image to Docker Hub"
                bat "docker tag digitalvisitorapp:v1 supriyamallesh/digitalvisitorapp:v1"
                bat "docker push supriyamallesh/digitalvisitorapp:v1"
            }
        }
        stage('Deploy to Kubernets')
        {
            steps{
                bat 'kubectl apply -f deployment.yaml --validate=false'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    post{
        success{
            echo 'Pipline completed successfully!'

        }
        failure{
            echo 'Pipeline failed, Please check the logs.'
        }
    }
}