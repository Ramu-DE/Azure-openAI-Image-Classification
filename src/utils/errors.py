"""Error handling utilities"""


class ClassificationError(Exception):
    """Base exception for classification errors"""
    pass


class ImageValidationError(ClassificationError):
    """Raised when image validation fails"""
    pass


class ConfigurationError(ClassificationError):
    """Raised when configuration is invalid"""
    pass
