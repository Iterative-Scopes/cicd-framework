# CICD CFG Action
load CI/CD pipeline profile for given environment settings 

## development 
- `make venv`
- make changes in python source code
- `make build`
- check in package file in the folder **dist**

## usage 
- `cicdcfg --env dev --role build --profile full-path`