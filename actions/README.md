# CI/CD Framework Reusable Actions
- CI/CD Framework actions are used in CI/CD Framework reusable workflows or project CI/CD pipelines
- each action has been in its owner folder

## aws-login
- setup AWS OpenID connection with following input arguments,
    - `AWS_REGION`: aws region 
    - `ROLE_ARN`:  aws assume role with account id

## build-ecr-image
- build and publish container image with following input arguments,
    - `aws_account`: aws account
    - `aws_role` : aws assume role
    - `aws_region` : aws region  
    - `ecr_repository`: ECR image repository name
    - `make_cmd` : make container image command
        - default value is **container**, it could be cpu or gpu in ML model project