MAKEFLAGS += --warn-undefined-variables --no-print-directory
SHELL := bash
.SHELLFLAGS := -eu -o pipefail -c
.DEFAULT_GOAL := all
.DELETE_ON_ERROR:
.SUFFIXES:

PROJECT ?= fun
ENVNAME ?= nonprod

.DEFAULT_GOAL := help

#help: @ List available commands
help:
	@grep -E '[a-zA-Z\.\-]+:.*?@ .*$$' $(MAKEFILE_LIST)| tr -d '#'  | awk 'BEGIN {FS = ":.*?@ "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

#k8s/create: @ Create K8S Cluster
k8s/create:
	@echo
	@echo Creating Kind cluster....
	@echo
	@kind create cluster
	@kubectl cluster-info --context kind-kind

#k8s/delete: @ Delete K8S Cluster
k8s/delete:
	@echo
	@echo Deleting Kind cluster....
	@echo
	@kind delete cluster

#k8s/config: @ Connect to the cluster
k8s/config:
	@echo
	@echo Connecting to cluster...
	@echo
	@kubectl config use-context kind-kind
	@kubectl get nodes --show-labels

#tf/init: @ Run Terraform Init
tf/init: k8s/config
	@echo
	@echo Initialising Terraform...
	@echo
	@terraform init
	@terraform fmt

#tf/plan: @ Run Terraform plan
tf/plan: tf/init 
	@echo
	@echo Planning Terraform...
	@echo
	@terraform plan \
		-var-file=params/$(ENVNAME).tfvars \
		-out=/tmp/$(PROJECT)-$(ENVNAME).tfplan

#tf/apply: @ Run Terraform apply
tf/apply:
	@echo
	@echo Planning Terraform...
	@echo
	@terraform apply /tmp/$(PROJECT)-$(ENVNAME).tfplan && \
		rm -f /tmp/$(PROJECT)-$(ENVNAME).tfplan

#tf/destroy: @ Run Terraform destroy
tf/destroy:
	@echo
	@echo Planning Terraform...
	@echo
	@terraform destroy

REQUIRED_IMAGES ?= docker.io/bitnami/mongodb:4.2.4-debian-10-r0 docker.io/library/busybox:1.29.3 docker.io/library/nginx:latest

#docker/pulls: @ Docker Pull Images
docker/pulls: k8s/config
	@echo
	@echo Pulling images for Kind...
	@echo
	@for img in $(REQUIRED_IMAGES); do \
		docker pull $$img ; \
		kind load docker-image $$img ; \
		done
