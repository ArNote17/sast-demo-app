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
                # Pastikan Python tersedia
                python3 --version
                
                # Buat virtual environment
                python3 -m venv venv

                # Aktifkan virtual environment
                . venv/bin/activate

                # Instal Bandit
                pip install bandit
                '''
            }
        }
        stage('SAST Analysis') {
            steps {
                sh '''
                # Aktifkan virtual environment
                . venv/bin/activate

                # Jalankan analisis Bandit
                bandit -f xml -o bandit-output.xml -r . || true
                '''
                
                // Rekam hasil analisis
                recordIssues tools: [bandit(pattern: 'bandit-output.xml')]
            }
        }
    }
}
