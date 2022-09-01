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

## build-lambda-package
- build Lambda package (Lambda container and Lambda Zip),
    - if Lambda package == ecr, this action builds Lambda container with follwing input arguments
        - `aws_region` : aws region 
        - `repository` : ecr image repository name
        - `env`: environment to push package
    - if Lambda package == Zip, this action builds Lambda Zip with follwing input arguments,
        - `registry` : s3 bucket name
        - `repository` : name of the package
        - `env`: environment to push package

## build-lambda-zip
- build lambda package, return zip uri with folowing input arguments,
    - `registry` : s3 bucket name
    - `repository` : name of the package

## build-source
- build and lint source code on branch/tag with following input arguments
    - `runtime`:runtime used in source code build (python|node)
    - `version`:runtime version (python_version|node_version)  

## cicdcfg
-  Reads CI/CD yaml configuration  with following input arguments,
    - `env`: environment running cicd workflow
    - `profile`: yaml config file (cicdprofile) for cicd workflow
    - `role`: auth role for cicd workflow,default value: `build` role

## connect2aws
- connect to AWS account associated with a given environment with following input arguments,
    - `env`: environment running cicd workflow
    - `role`: assume role to connect to AWS
    - `profile`: yaml config file (cicdprofile)

## deploy-lambda
-  deploys Lambda container with Image or S3 or Zip with following input arguments,
    - `env`: environment hosting lambda
    - `profile`: environment profile
    - `package_ref` : lambda Package reference from Lambda-build job
    - `role-to-assume` : assume role used to connect to AWS
    - `role-duration-seconds` : duration OIDC provider needs to directly assume an IAM Role
    - `aws-region`: aws region
    - `repository`: ecr image repository name
    - `audience`: OpenID connnection client 

## get-ecr-image-uri
- gets ecr image by image tag after aws authentication with follwoing input arguments,
    - `aws_region` : aws region 
    - `repository` : ecr image repository name
    - `image_tag`: image tag
    - `registry`: ecr registry

## Integration-testing
- runs integration testing in a given environment with following input arguments,
    - `env`: environment to run tests
    - `profile`: yaml config file (cicdprofile)

## map-ref2env
- mapping GitHub Ref to IS environment and echo environmnet name based on githubref_type
    - if `githubref ==  branch` && `githubref == main`, env=dev
    - if `githubref ==  branch` && `githubref == nonmain`, env=qa
    - if `githubref ==  tag`, env= staging

## next-release
- composing the next release version with following input arguments,
    - `versionincrement`: increment the MAJOR,MINOR, or the PATCH

## python-build
- runs make file to build, test, lint and coverage reports of the application with input arguments,
    - `python_version`: runtime python version

## unit-testing
- runs unit testing on source code after source build in the same runner with input arguments,
    - `docker-compose`: docker compose file

## validate-rc-tag
- Validate rc tags and checks if input tag match the semver scheme with follwoing input arguments,
    - `tag`: RC tag name   
