

help: ## show commands
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

venv: ## setup virtual enviroment and install depedencies
venv:
	@echo "create venv..."

build: ## create a release
build: 
	@echo "build pkg..."


lint: ## check code style and security
lint:
	@echo "code linting..."

unittest: ## run unit testing
unittest:
	@echo "unit testing"


integrationtest: ## test lambda container
integrationtest:
	@echo "integration testing..."


container: ## build container image
container: 
	@echo "build dockeer container image..."

ifdef remotereg
		@echo "docker image tag $(PACKAGE_NAME) $(remotereg):$(tag)"
endif

containertest: ## test lambda container
containertest:
	@echo "container testing..."	

clean: ##clean venv and cached files
clean:
	@echo "clean..."
