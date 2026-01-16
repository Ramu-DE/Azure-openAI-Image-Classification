"""Main classification engine using Azure OpenAI GPT-4o"""

import base64
from openai import AzureOpenAI
from typing import Dict, Any


class ImageClassifier:
    """Image classifier using Azure OpenAI GPT-4o vision capabilities"""
    
    def __init__(self, client: AzureOpenAI, deployment_name: str):
        self.client = client
        self.deployment_name = deployment_name
    
    def classify_image(self, image_path: str, classes: list) -> Dict[str, Any]:
        """Classify a single image"""
        with open(image_path, "rb") as f:
            image_data = base64.b64encode(f.read()).decode("utf-8")
        
        prompt = f"Classify this flower image into one of: {', '.join(classes)}. Return only the class name."
        
        response = self.client.chat.completions.create(
            model=self.deployment_name,
            messages=[{
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{image_data}"}}
                ]
            }],
            max_tokens=50
        )
        
        prediction = response.choices[0].message.content.strip().lower()
        return {"prediction": prediction, "image_path": image_path}
