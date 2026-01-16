"""Batch processing example"""

import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.core.classifier import ImageClassifier
from src.batch.processor import BatchProcessor
from src.export.formatters import ResultFormatter

# Load environment variables
load_dotenv('azure.env')

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize classifier and batch processor
classifier = ImageClassifier(
    client=client,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)
processor = BatchProcessor(classifier, batch_size=10)

# Process directory
classes = ["dandelion", "rose", "sunflower", "daisy"]
results = processor.process_directory("flowers_images/class1", classes)

# Export results
ResultFormatter.to_json(results, "results.json")
ResultFormatter.to_csv(results, "results.csv")

print(f"Processed {len(results)} images")
