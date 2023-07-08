.DEFAULT_GOAL := help
SHELL = /usr/bin/env bash -o pipefail
.SHELLFLAGS = -ec
.PHONY: init test

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-18s\033[33m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

##@ --| Python    |--------------------------------------------------------------------------------------------------------------------------------------

test: check-tools ## Run pytest
	clear ; \
	printf " \n"; \
	pytest -sv ; \
	printf " \033[36m-------------------------------------------\033[0m\n"; \
	printf " \033[36mDone! (pytest)\033[0m\n"; \
	printf " \033[36m-------------------------------------------\033[0m\n"; \
	printf " \n"; \


venv-on: check-tools ## Start .venv Python Virtual Environment
	@printf " \n"; \
	printf " \033[36mrun: \033[33msource .venv/bin/activate\033[0m\n"; \
	printf " \n"; \

venv-off: check-tools ## Leave .venv Python Virtual Environment
	@printf " \n"; \
	printf " \033[36mrun: \033[33mdeactivate\033[0m\n"; \
	printf " \n"; \

##@ --| Utils     |--------------------------------------------------------------------------------------------------------------------------------------

# chk-code:  ## Code checking with python tools: quality, format, security
# 	clear ; \
# 	./scripts/run-checks.sh ; \
# 	printf " \033[36m-------------------------------------------\033[0m\n"; \
# 	printf " \033[36mDone! (checks)\033[0m\n"; \
# 	printf " \033[36m-------------------------------------------\033[0m\n"; \
# 	printf " \n"; \

# chk-code-act:  ## Code checking and perform actions (if needed), python tools
# 	clear ; \
# 	./scripts/run-checks.sh perform-actions; \
# 	printf " \033[36m-------------------------------------------\033[0m\n"; \
# 	printf " \033[36mDone! (checks)\033[0m\n"; \
# 	printf " \033[36m-------------------------------------------\033[0m\n"; \
# 	printf " \n"; \

init:  ## Install Python dependencies (dev and runtime)
	clear ; \
	pip-compile --output-file requirements.txt requirements.in requirements-dev.in ; \
	printf " \033[36m-------------------------------------------\033[0m\n"; \
	printf " \033[36mDone! (install deps)\033[0m\n"; \
	printf " \033[36m-------------------------------------------\033[0m\n"; \
	printf " \n"; \

check-tools: # Check if the necessary tools are installed
ifneq (,$(which python))
	$(error "Python not installed!")
endif


## (INTERNAL) Check if the necessary environment variable are set
check-var-stacks:
	@ if [ "${STACKS}" = "" ]; then \
		printf "\n"; \
		printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
		printf " \033[36m Parameter STACKS not informed \033[33m$*\033[36m not set\033[0m\n"; \
		printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
		printf "\n"; \
		exit 1; \
	fi

## (INTERNAL) Check if the necessary environment variable are set
check-envvars: 
	$(MAKE) -s envvar-CDK_DEVELOPMENT_ACCOUNT; \
	$(MAKE) -s envvar-CDK_DEVELOPMENT_REGION; \
	$(MAKE) -s envvar-CDK_PREPROD_ACCOUNT; \
	$(MAKE) -s envvar-CDK_PREPROD_REGION; \
	$(MAKE) -s envvar-CDK_PIPELINE_ACCOUNT; \
	$(MAKE) -s envvar-CDK_PIPELINE_REGION; \
	$(MAKE) -s envvar-CDK_PRODUCTION_ACCOUNT; \
	$(MAKE) -s envvar-CDK_PRODUCTION_REGION; \
	$(MAKE) -s envvar-VIRTUAL_ENV; \

## (INTERNAL) Check if the necessary environment variable for bootstrap are set
check-boot-envvars: 
	$(MAKE) -s envvar-CDK_BOOTSTRAP_ACCOUNT; \
	$(MAKE) -s envvar-CDK_BOOTSTRAP_REGION; \

## (INTERNAL) Check if the environment variable is set
envvar-%: 
	@ if [ "${${*}}" = "" ]; then \
	    if [[ "$*" == "VIRTUAL_ENV" ]]; then \
			printf "\n"; \
			printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
			printf " \033[36m Python Virtual Environment \033[37mNOT \033[33mactivated\033[0m\n"; \
			printf " \033[36m Run: \033[33msource .venv/bin/activate\033[0m\n"; \
			printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
			printf "\n"; \
		else \
			printf "\n"; \
			printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
			printf " \033[36m Environment variable \033[33m$*\033[36m not set\033[0m\n"; \
			printf " \033[37m Run: \033[33msource ./scripts/set-env.sh\033[0m\n"; \
			printf " \033[36m---------------------------------------------------------------\033[0m\n"; \
			printf "\n"; \
		fi; \
		exit 1; \
    fi

define generate_random
{ \
set -e ; \
TMP_RND="$(2)$$(tr -dc a-z0-9 </dev/urandom  | head -c $(1) ; echo '')" ; \
}
endef

