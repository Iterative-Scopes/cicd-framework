# CI/CD Workflow
IS sharable GitHub actions and workflows, which are used to develop IS application CI/CD pipeline

## Code Structure 

### /actions/
- contains sharable actions
- one action per subfolder 
- [GitHub custom action development](https://docs.github.com/en/actions/creating-actions/about-custom-actions)

### /.github/workflows/
- contains sharable workflows 
- one workflow per file
- [GitHub sharable workflow development](https://docs.github.com/en/actions/using-workflows/reusing-workflows)

### /templates/
- contains templates of CI/CD framework, such as 
    - makefile as source code build tool


## Development Practices
- name 
    - make short, but readable and meaningful with separating word with **-**
    - use following naming convention if 
        - runtime specific in prefix, such as python-<name> or js-<name>
        - app specific in suffix, such as python-<name>-ml for ML team



