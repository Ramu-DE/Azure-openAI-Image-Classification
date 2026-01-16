"""Alerting system for monitoring"""

from typing import Callable, List


class AlertSystem:
    """Manages alerts for system events"""
    
    def __init__(self):
        self.alerts = []
        self.handlers = []
    
    def add_handler(self, handler: Callable) -> None:
        """Add alert handler"""
        self.handlers.append(handler)
    
    def trigger_alert(self, message: str, severity: str = "INFO") -> None:
        """Trigger an alert"""
        alert = {"message": message, "severity": severity}
        self.alerts.append(alert)
        
        for handler in self.handlers:
            handler(alert)
    
    def get_alerts(self) -> List:
        """Get all alerts"""
        return self.alerts
