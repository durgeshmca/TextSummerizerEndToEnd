# TextSummerizerEndToEnd
An End to End text summarize project


## Workflows
Update the followings
1.  config/config.yaml
2.  params.yaml
3.  src/TextSummarizer/entity
4.  configuration manager in src/TextSummarizer/config
5.  src/TextSummarizer/components
6.  src/TextSummarizer/pipeline
7.  main.py
8.   app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/durgeshmca/TextSummerizerEndToEnd
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create --prefix ./env summary python=3.11 -y
```

```bash
conda activate ./env
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


```bash
Author: Durgesh Chandra Mishra
Data Scientist
Email: durgeshcmishra@live.in

```



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 936272926283.dkr.ecr.ap-south-1.amazonaws.com/textsum

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = 936272926283.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = textsum