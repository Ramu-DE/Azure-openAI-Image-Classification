"""External system integrations"""

import requests
from typing import Dict, Any


class ExternalIntegration:
    """Handles integration with external systems"""
    
    def __init__(self, webhook_url: str = None):
        self.webhook_url = webhook_url
    
    def send_webhook(self, data: Dict[str, Any]) -> bool:
        """Send data to webhook endpoint"""
        if not self.webhook_url:
            return False
        
        try:
            response = requests.post(self.webhook_url, json=data, timeout=10)
            return response.status_code == 200
        except Exception:
            return False
