"""Performance monitoring system"""

import time
from typing import Dict, List


class PerformanceMonitor:
    """Monitors classification performance metrics"""
    
    def __init__(self):
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "total_time": 0.0
        }
    
    def record_request(self, success: bool, duration: float) -> None:
        """Record a classification request"""
        self.metrics["total_requests"] += 1
        if success:
            self.metrics["successful_requests"] += 1
        else:
            self.metrics["failed_requests"] += 1
        self.metrics["total_time"] += duration
    
    def get_metrics(self) -> Dict:
        """Get current metrics"""
        avg_time = self.metrics["total_time"] / self.metrics["total_requests"] if self.metrics["total_requests"] > 0 else 0
        return {
            **self.metrics,
            "average_time": avg_time,
            "success_rate": self.metrics["successful_requests"] / self.metrics["total_requests"] if self.metrics["total_requests"] > 0 else 0
        }
