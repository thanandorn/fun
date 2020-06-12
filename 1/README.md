# 3-Tier Application - Hypothesis Infrastructure

## Application Tiers

 - Frontend
 - Backend
 - Database (MongoDB)

## Infra Components

 - Kubernetes Cluster ([Kind](https://kind.sigs.k8s.io/))
 - Terraform
 - Makefile

### Initialising 

 - Create Kubernetes cluster

```
$ make 
help                           List available commands
k8s/create                     Create K8S Cluster
k8s/delete                     Delete K8S Cluster
k8s/config                     Connect to the cluster
tf/init                        Run Terraform Init
tf/plan                        Run Terraform plan
tf/apply                       Run Terraform apply
tf/destroy                     Run Terraform destroy
docker/pulls                   Docker Pull Images

$ make k8s/create 

Creating Kind cluster....

Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.18.2) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a question, bug, or feature request? Let us know! https://kind.sigs.k8s.io/#community 🙂

```

 - Manually populate Docker images onto the cluster. [Known-Issue](https://kind.sigs.k8s.io/docs/user/known-issues/#unable-to-pull-images)

```
make docker/pulls

Connecting to cluster...

Switched to context "kind-kind".
NAME                 STATUS   ROLES    AGE     VERSION   LABELS
kind-control-plane   Ready    master   8m31s   v1.18.2   beta.kubernetes.io/arch=amd64,beta.kubernetes.io/os=linux,kubernetes.io/arch=amd64,kubernetes.io/hostname=kind-control-plane,kubernetes.io/os=linux,node-role.kubernetes.io/master=

Pulling images for Kind...

4.2.4-debian-10-r0: Pulling from bitnami/mongodb
Digest: sha256:85f9e2064f2170abc397ad986ffe798ed2b5444ff23e4406838aa010b6990648
Status: Image is up to date for bitnami/mongodb:4.2.4-debian-10-r0
docker.io/bitnami/mongodb:4.2.4-debian-10-r0
1.29.3: Pulling from library/busybox
Digest: sha256:8ccbac733d19c0dd4d70b4f0c1e12245b5fa3ad24758a11035ee505c629c0796
Status: Image is up to date for busybox:1.29.3
docker.io/library/busybox:1.29.3
latest: Pulling from library/nginx
Digest: sha256:21f32f6c08406306d822a0e6e8b7dc81f53f336570e852e25fbe1e3e3d0d0133
Status: Image is up to date for nginx:latest
docker.io/library/nginx:latest
```

  - Standing up services on nonprod environment with Terraform 
  - Clean up
[![asciicast](https://asciinema.org/a/v9Qr8UVKjiu1KHouE8g56tC67.svg)](https://asciinema.org/a/v9Qr8UVKjiu1KHouE8g56tC67)


