# API Reference

## Core Components

### ImageClassifier

Main classification engine using Azure OpenAI GPT-4o.

```python
from src.core.classifier import ImageClassifier

classifier = ImageClassifier(client, deployment_name)
result = classifier.classify_image(image_path, classes)
```

### BatchProcessor

Process multiple images efficiently.

```python
from src.batch.processor import BatchProcessor

processor = BatchProcessor(classifier, batch_size=10)
results = processor.process_directory(directory, classes)
```

### ResultFormatter

Export results in multiple formats.

```python
from src.export.formatters import ResultFormatter

ResultFormatter.to_json(results, "output.json")
ResultFormatter.to_csv(results, "output.csv")
ResultFormatter.to_xml(results, "output.xml")
```

## Configuration

### ConfigManager

Manage domain and system configurations.

```python
from src.core.config_manager import ConfigManager

config = ConfigManager("config/domains.yaml")
domain_config = config.get_domain_config("flowers")
```

## Monitoring

### PerformanceMonitor

Track classification performance metrics.

```python
from src.monitoring.performance import PerformanceMonitor

monitor = PerformanceMonitor()
monitor.record_request(success=True, duration=1.5)
metrics = monitor.get_metrics()
```
