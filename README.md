# DPS-AI-Challenge

The task for this challenge was to train a basic regression model with TensorFlow using Google's ML platform Vertex AI. The dataset that was used was the [Auto MPG dataset](https://www.kaggle.com/uciml/autompg-dataset) from Kaggle and the task was to predict fuel efficiency of a vehicle. This [tutorial](https://codelabs.developers.google.com/codelabs/vertex-ai-custom-models#2) was used as a guide through the whole process. What follows below is a description of the full process for solving the challange:

## Setting up the environment
The first part was a technical part of setting up the environment for the project. It consisted of creating a new project on the Cloud Console, activating the cloud shell, enabling the necessary APIs, creating a cloud storage bucket (for storing saved model assets), and ensuring the usage of Python 3 when running the scripts. The following had to be enabled: Compute Engine, Container Registry, and Vertex AI services.
```shell
gcloud services enable compute.googleapis.com
gcloud services enable containerregistry.googleapis.com
gcloud services enable aiplatform.googleapis.com                 
```
![APIs](/img/enableAPIs.jpg)

## Containarizing the code
In order to submit the training job to Vertex AI, the first step was to put the training code into a Docker container. The files ```Dockerfile``` and ```train.py``` were created in this part. The code in ```train.py``` is adapted from the appropriate tutorial in the tensorflow documentation. To build the container the following commands were used
```shell
IMAGE_URI="gcr.io/$GOOGLE_CLOUD_PROJECT/mpg:v1"
docker build ./ -t $IMAGE_URI
docker push $IMAGE_URI
```
![docker_build](/img/docker.jpg)

```shell
docker push $IMAGE_URI
```
![docker_push](/img/docker_push.jpg)

## Training
Now came the main part - the actual training of the model. Custom training option was used for this purpose, instead of the AutoML, as well as the custom Docker container. The machine type used for this purpose was the **n1-standard-4** (4vCPUs, 15 GB memory). Here is the trained model summary:
![Model summary](/img/trained_model.jpg)

Additionally, a short video describing the workflow for solving the challenge can be found under the ```video``` directory.

## Creating an endpoint for the trained model
For the purpose of creating a model resource and deploying it to an endpoint, the ```deploy.py``` file was created. The following command was executed from the root directory:
```shell
python3 deploy.py | tee deploy-output.txt
```
Output:
```console
INFO:google.cloud.aiplatform.models:Endpoint model deployed. Resource name: projects/929310466514/locations/us-central1/endpoints/2947333277230301184
```

## Getting predictions
Finally, the goal is to obtain the predictions of the model. Specifically, for this challenge, the predictions for the input ```test_mpg = [1, 2, 3, 2, -2, -1, -2, -1, 0]```. To get the predictions, the file ```predict.py``` was created with the appropriate testing example and the endpoint of our deployed model. Finally, the predictions were obtained by running the script:
```shell
python3 predict.py
```
And the output was:
```console
API response:  Prediction(predictions=[[17.07827]], deployed_model_id='3038003404103221248', explanations=None)
Predicted MPG:  17.07827
```

## Bonus
For the bonus part, I built another model for the task of sentiment analysis with TensorFlow, using IMDB data set. The tutorial I followed can be found [here](https://www.tensorflow.org/tutorials/keras/text_classification). The end-to-end process was analogous to the original challenge task. All relevant files, including the code, can be found under the directory ```textcl```.
