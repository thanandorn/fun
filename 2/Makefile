MAKEFLAGS += --warn-undefined-variables --no-print-directory
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

.DEFAULT_GOAL := help

ifndef AWS_DEFAULT_PROFILE
$(error AWS_DEFAULT_PROFILE is not set)
endif

#help: @ List available commands
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST)| tr -d '#'  | awk 'BEGIN {FS = ":.*?@ "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#test: @ Running Unittest Module
test:
	@echo Running UnitTest....
	@python -m unittest metadata_finder_test.py

