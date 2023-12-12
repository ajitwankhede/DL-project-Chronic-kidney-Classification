**Deep Learning Project Chronic Kidney Classification**

Project flow
1.	Project templet creation
2.	Project setup and requirement installation
3.	Logging, Utils and exception Module
4.	Project workflow
5.	Notebook Experiment
6.	Modular code implementation
7.	Training pipeline
8.	MLflow (MlOPs tool) – For experiment tracking and model registration
9.	DVC (MLOps tool) – for pipeline tracking  and implementation
a.	DVC : Data version control
10.	Prediction pipeline and User app creation
11.	Docker
12.	Final CI/CD Development
    
Task:
Build deep learning base Image classification model which able to classify, CT scan image of kidney and identify kidney with tumour and Normal kidney.

Dataset:
I am using dataset of Kidney CT Scan image, which is identified and classified as kidney with tumour and Normal kidney with respective to image.

For example:

### **Normal kidney**

 ![Normal- (709)](https://github.com/ajitwankhede/DL-project-Chronic-kidney-Classification/assets/85306409/df0eb302-b340-4373-8770-c0b56d4c9e55)

 ### **Tumour Kidney**
 
![Tumor- (811)](https://github.com/ajitwankhede/DL-project-Chronic-kidney-Classification/assets/85306409/1b793724-0ae2-467d-9575-a73d56f14423)

### **App UI**

![Screenshot 2023-12-12 084604](https://github.com/ajitwankhede/DL-project-Chronic-kidney-Classification/assets/85306409/81bdb6f4-0946-48e2-886d-b91a7cd3cd0e)

### Download Database: 

Small Size : https://drive.google.com/file/d/1BIiJfOdei5xm9XMw_Gq9Bdq8uQWFtSPC/view?usp=sharing

Full Size Dataset: https://www.kaggle.com/datasets/nazmul0087/ct-kidney-dataset-normal-cyst-tumor-and-stone



## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository


```bash
[(https://github.com/ajitwankhede/DL-project-Chronic-kidney-Classification.git)]
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
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


## MLflow

- [Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https: <Add dagshub URL> \
MLFLOW_TRACKING_USERNAME= <Add User name> \
MLFLOW_TRACKING_PASSWORD= <Add Password> \
python script.py

Run this to export as env variables:

```bash

c <Add dagshub URL>

export MLFLOW_TRACKING_USERNAME= <Add User name>

export MLFLOW_TRACKING_PASSWORD= <Add Password>

```


```bash

"export" not work !!!
Use Git bash terminal in VS code insted powershell or CMD

```

### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag


## About MLflow & DVC

MLflow

 - Its Production Grade
 - Trace all of your expriements
 - Logging & taging your model


DVC 

 - Its very lite weight for POC only
 - lite weight expriements tracker
 - It can perform Orchestration (Creating Pipelines)



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
    - Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/project

	
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

    AWS_ECR_LOGIN_URI = demo>>  566373416292.dkr.ecr.ap-south-1.amazonaws.com

    ECR_REPOSITORY_NAME = simple-app

### DVC Pipeline Flow

![Screenshot 2023-12-06 002122](https://github.com/ajitwankhede/DL-project-Chronic-kidney-Classification/assets/85306409/edb2239c-8cc4-456b-b9eb-6851c7a40e34)

# Future Scope
	- Enable gpu training
	- Train model on full data with all class.
	- Improve UI
