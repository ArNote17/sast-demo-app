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
                # Buat virtual environment
                python3 -m venv venv

                # Aktifkan virtual environment
                . venv/bin/activate

                # Instal bandit di dalam virtual environment
                pip install bandit
                '''
            }
        }
        stage('SAST Analysis') {
            steps {
                sh '''
                # Aktifkan virtual environment
                . venv/bin/activate

                # Jalankan bandit untuk analisis
                bandit -f xml -o bandit-output.xml -r . || true
                '''
                
                // Rekam hasil analisis
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
