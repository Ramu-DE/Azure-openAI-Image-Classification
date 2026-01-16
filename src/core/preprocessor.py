"""Image preprocessing and validation"""

from PIL import Image
from typing import Tuple


class ImagePreprocessor:
    """Handles image preprocessing and validation"""
    
    def __init__(self, max_size: Tuple[int, int] = (1024, 1024)):
        self.max_size = max_size
    
    def validate_image(self, image_path: str) -> bool:
        """Validate image format and integrity"""
        try:
            with Image.open(image_path) as img:
                img.verify()
            return True
        except Exception:
            return False
    
    def resize_image(self, image_path: str, output_path: str) -> None:
        """Resize image while maintaining aspect ratio"""
        with Image.open(image_path) as img:
            img.thumbnail(self.max_size, Image.Resampling.LANCZOS)
            img.save(output_path)
