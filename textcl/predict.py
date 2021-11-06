from google.cloud import aiplatform

endpoint = aiplatform.Endpoint(
    endpoint_name="projects/929310466514/locations/us-central1/endpoints/2947333277230301184"
)

# A test example we'll send to our model for prediction
examples = [
  "The movie was great!",
  "The movie was okay.",
  "The movie was terrible..."
]


response = endpoint.predict([examples])

print('API response: ', response)

print('Predicted labels: ', response.predictions[0])
