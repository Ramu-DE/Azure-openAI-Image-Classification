"""Logging utilities"""

import logging
import sys


def setup_logging(level: str = "INFO") -> logging.Logger:
    """Setup logging configuration"""
    logger = logging.getLogger("image_classification")
    logger.setLevel(getattr(logging, level.upper()))
    
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger
