# CI/CD Reusable Workflows
 - this folder contains reusable workflows, which can be used for a project CI/CD pipeline or GetHub Starter workflow.
 - a caller needs to set permissions and GitHub events to use a sharable workflow

## python-build-container
- build workflow includes, 
    - check out source code on a active branch or tag
    - build python source code with linting, unit testing and package creation 
    - create and publish container image to ECR with branch or tag as deployable artifact
    - **Notes**, caller should not use the checkout action
        ```actions/checkout@v3```
- input arguments,
    - `python_version`: python version
    - `aws_account`: aws account
    - `aws_role` : aws assume role w/o account id
    - `aws_region` : aws region
    - `ecr_repository` : ECR container image name
 

