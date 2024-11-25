pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/ArNote17/sast-demo-app',
                    credentialsId: 'github-pat'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                # Verifikasi versi Python
                python3 --version
                
                # Instal bandit menggunakan pip3
                pip3 install bandit
                '''
            }
        }
        stage('SAST Analysis') {
            steps {
                sh '''
                # Jalankan Bandit untuk analisis statis
                bandit -f xml -o bandit-output.xml -r . || true
                '''
                // Rekam hasil analisis dengan Jenkins plugin
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
