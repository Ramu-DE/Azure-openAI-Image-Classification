"""Custom domain configuration example"""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.core.classifier import ImageClassifier
from src.core.config_manager import ConfigManager

# Load environment variables
load_dotenv('azure.env')

# Initialize configuration manager
config_manager = ConfigManager("config/domains.yaml")

# Get domain configuration
domain_config = config_manager.get_domain_config("flowers")
classes = domain_config.get("classes", [])

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

# Classify image using domain configuration
result = classifier.classify_image("flowers_images/class1/dandelion (1).jpg", classes)
print(f"Domain: flowers")
print(f"Prediction: {result['prediction']}")
