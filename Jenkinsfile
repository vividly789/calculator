node
{
    stage ('checkout code')
    {
        checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/vividly789/calculator.git']]])
    }
    stage ('code analysis')
    {
        echo "testing"
    }
}
