# HelloLambda
Example of an AWS Lambda function written in Python   

## Setup

### 1. configs.json

For this to work you need to create a copy of the **configs.json.template** file 
called configs.json and fill in the empty values.


For the *GITHUB_TOKEN* value you need to create and include a personal Github API 
token. See the following link for how to do that:


[https://github.com/blog/1509-personal-api-tokens](https://github.com/blog/1509-personal-api-tokens "Personal API Tokens")

### 2. Virtual Environment

Next you need to create a Python 2.7 virtual environment inside the HelloLambda
project in a folder called **venv_py27** and install the following packages:

    * PyGithub
    * six
    
both can be installed using the local pip that will be created with your 
virtual environment.

## Deploy

To deploy this package you need to create a zip file. The **deploy.py** file is
designed to do just that. All you need to do is run:

```bash
python deploy.py
```
This will create a zip file called **hello_lambda.zip**, which you can then 
upload to AWS Lambda for use.
