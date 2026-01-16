"""Progress tracking for batch operations"""

from typing import Optional


class ProgressTracker:
    """Tracks progress of batch processing operations"""
    
    def __init__(self, total: int):
        self.total = total
        self.current = 0
    
    def update(self, increment: int = 1) -> None:
        """Update progress"""
        self.current += increment
    
    def get_progress(self) -> float:
        """Get current progress percentage"""
        return (self.current / self.total) * 100 if self.total > 0 else 0
    
    def __str__(self) -> str:
        return f"Progress: {self.current}/{self.total} ({self.get_progress():.1f}%)"
