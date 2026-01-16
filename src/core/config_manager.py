"""Configuration management system"""

import yaml
from typing import Dict, Any


class ConfigManager:
    """Manages system and domain configurations"""
    
    def __init__(self, config_path: str = "config/domains.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        try:
            with open(self.config_path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return self._get_default_config()
    
    def _get_default_config(self) -> Dict[str, Any]:
        """Return default configuration"""
        return {
            "flowers": {
                "classes": ["dandelion", "rose", "sunflower", "daisy"],
                "prompt_template": "Classify this flower image"
            }
        }
    
    def get_domain_config(self, domain: str) -> Dict[str, Any]:
        """Get configuration for specific domain"""
        return self.config.get(domain, {})
