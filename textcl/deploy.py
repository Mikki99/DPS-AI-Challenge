from google.cloud import aiplatform

# Create a model resource from public model assets
model = aiplatform.Model.upload(
    display_name="sentiment-analysis",
    artifact_uri="gs://dps-ai-challenge-bucket",
    serving_container_image_uri="gcr.io/dps-ai-challenge/textcl@sha256:240b1ead3de9bd7593e9cb75f5e052600f1d53269e2d27347c752628c1fec259"
)

# Deploy the above model to an endpoint
endpoint = model.deploy(
    machine_type="n1-standard-4"
)
