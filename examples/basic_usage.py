"""Basic usage example for image classification"""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.core.classifier import ImageClassifier

# Load environment variables
load_dotenv('azure.env')

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize classifier
classifier = ImageClassifier(
    client=client,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)

# Classify a single image
classes = ["dandelion", "rose", "sunflower", "daisy"]
result = classifier.classify_image("flowers_images/class1/dandelion (1).jpg", classes)

print(f"Prediction: {result['prediction']}")
print(f"Image: {result['image_path']}")
