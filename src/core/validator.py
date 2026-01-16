"""Result validation and post-processing"""

from typing import Dict, Any, List


class ResultValidator:
    """Validates and normalizes classification results"""
    
    def __init__(self, valid_classes: List[str]):
        self.valid_classes = [c.lower() for c in valid_classes]
    
    def validate_result(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """Validate and normalize classification result"""
        prediction = result.get("prediction", "").lower()
        
        if prediction in self.valid_classes:
            result["valid"] = True
            result["normalized_prediction"] = prediction
        else:
            result["valid"] = False
            result["normalized_prediction"] = self._find_closest_match(prediction)
        
        return result
    
    def _find_closest_match(self, prediction: str) -> str:
        """Find closest matching class"""
        for valid_class in self.valid_classes:
            if valid_class in prediction or prediction in valid_class:
                return valid_class
        return self.valid_classes[0]
