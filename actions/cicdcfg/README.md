# CICD CFG Action
load CI/CD pipeline profile for given environment settings 

## development 
- `make venv`
- make changes in python source code
- `make build`
- check in package file in the folder **dist**

## usage 
- `cicdcfg --env dev --role build --profile full-path`

## test on repo
- `cicdcfg --env dev --role build --profile $PWD/.cicd-profile.yml`
- check outputs 

## Semantic Versioning
- Increase the version of tar package by 1 for new changes
- Current version `0.2.0` and the file name is  `cicdcfg-0.2.0.tar.gz` 