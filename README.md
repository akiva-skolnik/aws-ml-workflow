# Deploy and monitor a machine learning workflow for Image Classification

## Introduction
In this project we implement a simple classification task: predict bicycle / motorcycleusing the CIFAR dataset.
The main focus of the project is to deploy and monitor the machine learning workflow in AWS.

## Steps
The full work can be seen in the notebook `ML_Workflow.ipynb`. The main steps are:
1. Load the CIFAR dataset, transform, and upload to S3.
2. Train a simple model using the SageMaker framework image-classification.
3. Deploy the model with monitoring and create an endpoint, while verifying we can make predictions.
4. Next, we leave the notebook and create 3 Lambda functions to make predictions (get image, classify, and warn on low confidence). See the `lambdas` folder.
5. We glue them together in a Step Function (see `step_function` folder).
6. Finally, we make some predictions and plot custom graphs to monitor the workflow.
