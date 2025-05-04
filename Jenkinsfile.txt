pipeline {
    agent any

    environment {
        EC2_USER = "ubuntu"
        EC2_HOST = "18.222.119.100"
        PROJECT_DIR = "/home/ubuntu/DjangoProject"
    }

    triggers {
        githubPush()
    }

    stages {
        stage('Update Code on EC2') {
            steps {
                script {
                    // Use SSH agent inside steps
                    sshagent (credentials: ['ec2-ssh-private-key']) {
                        sh """
                            ssh -o StrictHostKeyChecking=no ${EC2_USER}@${EC2_HOST} '
                                cd ${PROJECT_DIR}
                                git pull origin main
                                python3 -m venv myEnv
                                source myEnv/bin/activate
                                python3 -m pip install -r requirements.txt
                            '
                        """
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Code updated and app restarted successfully on EC2!"
        }
        failure {
            echo "Deployment failed."
        }
    }
}
