pipeline {
  agent any
  tools {
        maven 'Maven_3_8_7'
    }
   stages{
    stage('CompileandRunSonarAnalysis') {
            steps {
		sh 'mvn clean verify sonar:sonar -Dsonar.projectKey=TestingDevSecOps123 -Dsonar.organization=TestingDevSecOps123 -Dsonar.host.url=https://sonarcloud.io -Dsonar.token=499daf469dbb1ae7e1a14e00ba5a45df790952cd'
			}
        }
  }
}
