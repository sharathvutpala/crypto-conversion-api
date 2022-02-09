# crypto-conversion-api

This repo consists of 
- A webservice written in Python using FastAPI that returns the spot price of BTC(Bitcoin) from Coinbase for different Currencies. 
- Tests which can be run with pytest framework
- Code for setting up EKS cluster using Terraform
- Helm Chart for deploying the application to EKS cluster
- Dockerfile for containerizing the webservice
- Github workflows for building docker image and running test cases, and deploying helm chart to EKS 

## Prerequisites
- AWS Account
- AWS CLI
- Terraform
- aws-iam-authenticator
- kubectl

### EKS Cluster Provisioing with Terraform

I used Terraform for provisioning the EKS cluster. Before running terraform commands, make sure that terraform binary is installed, aws cli is configuered properly with required permissions, aws-iam-authenticator is installed. Once all the steps are completed, navigate to eks-infra directory for running terraform commands. 

```
cd eks-infra/
terraform init
```
No remote backend is configured, so state will be stored locally only. 

```
terraform plan
terraform apply 
```

This will generate a Kubeconfig file in the current directory, that is eks-infra. To access the cluster, we have to configure the kubectl to read from the newly generated config. This can be done in two ways:

1. Export Kubeconfig generated after terrafrom apply - 

```
export KUBECONFIG=kubeconfig_crypto-api-eks
```

2. Running aws eks subcommand

```
aws eks update-kubeconfig --region us-east-2 --name crypto-api-eks
```

## Helm Chart

A helm chart is available under k8s-helm/crypto-api directory. Contents of the chart are:
- Chart.yaml: Information about the chart and a sub chart is added under dependencies for nginx-ingress controller 
- Charth.lock: To build charts/ directory for sub charts, in this case ingress-nginx
- templates
  - acme-clusterissuer.yaml : A ClusterIssuer for issuing Let's Encrypt certificates using Cert-Manager
  - deployment.yaml: Deploing the webservice
  - service.yaml: A ClusterIP Service
  - Ingress: Managing external access to the service
- values.yaml: Configurable values for the helm chart

### Github workflows

There are 3 workflows available in the repo.
- docker-build.yml: For building and pushing the Docker container from Dockerfile present in the repo
- test.yaml: Running test cases using Pytest
- helm-deploy.yaml: Deploying Helm Chart to EKS Cluster. This step does 3 things
  - Runs helm dependency build to get the sub chart, that is ingress-nginx
  - Installs Cert-Manager helm chart separately ( Cert Manager cannot be installed as a sub chart due to some limitations)
  - Installs application helm chart which runs our webservice

NOTE: **Running deployment workflow will output address of the Nginx Ingress Controller, which need to be mapped to the host mentioned in the ingress configuration. **

### API  && Endpoints

Currently API can be accessible at https://crypto-api-demo.sharath.tech. This domain is mapped to load balancer created for Nginx Ingress Controller. It supports two endpoints. 
- /currency/<3 Letter Currnecy Code>: For example, /currency/USD. 
This endpoint support only these Currencies: [ USD, EUR, RUB, CAD, PHP, DKK]

- /health - This returns the health of the API, Status code 200 when API is healthy


### Future Scope

- A /metrics endpoint can be added to report health or metrics
- Integrating slack messaging in the application 
- More test cases

