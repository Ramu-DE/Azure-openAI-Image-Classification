"""Batch processing engine"""

import os
from typing import List, Dict, Any
from ..core.classifier import ImageClassifier


class BatchProcessor:
    """Processes multiple images in batches"""
    
    def __init__(self, classifier: ImageClassifier, batch_size: int = 10):
        self.classifier = classifier
        self.batch_size = batch_size
    
    def process_directory(self, directory: str, classes: List[str]) -> List[Dict[str, Any]]:
        """Process all images in a directory"""
        results = []
        image_files = [f for f in os.listdir(directory) if f.endswith(('.jpg', '.jpeg', '.png'))]
        
        for image_file in image_files:
            image_path = os.path.join(directory, image_file)
            result = self.classifier.classify_image(image_path, classes)
            results.append(result)
        
        return results
