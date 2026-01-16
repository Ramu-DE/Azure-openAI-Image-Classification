# Enhanced Image Classification Pipeline

An advanced, production-ready image classification system built on Azure OpenAI GPT-4o, designed for multi-domain classification with robust batch processing, monitoring, and extensibility.

## 🚀 Features

### Core Capabilities
- **Multi-Domain Classification**: Support for flowers, animals, objects, and custom domains
- **Batch Processing**: Efficient processing of large image datasets with progress tracking
- **Confidence Scoring**: Uncertainty detection and validation workflows
- **Performance Monitoring**: Real-time analytics, cost tracking, and alerting
- **Multiple Export Formats**: JSON, CSV, XML with comprehensive metadata

### Production Ready
- **Modular Architecture**: Plugin-based design for easy extension
- **Comprehensive Error Handling**: Graceful degradation and detailed logging
- **Rate Limiting**: Respects Azure OpenAI API limits with exponential backoff
- **Image Preprocessing**: Format validation, resizing, and quality checks
- **REST API**: External system integration with webhook support

## 📊 Current Performance

The original flower classification achieves **97% accuracy** on the test dataset:
- **Domains**: Flowers (dandelion, rose, sunflower, daisy)
- **Dataset**: 40 images (10 per class)
- **Model**: Azure OpenAI GPT-4o with vision capabilities

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│  Image Input    │───▶│ Image Preprocessor│───▶│Classification   │
└─────────────────┘    └──────────────────┘    │    Engine       │
                                               └─────────────────┘
┌─────────────────┐    ┌──────────────────┐           │
│ Configuration   │───▶│  Batch Processor │           ▼
│   Manager       │    └──────────────────┘    ┌─────────────────┐
└─────────────────┘                            │ Result Validator│
                                               └─────────────────┘
┌─────────────────┐    ┌──────────────────┐           │
│ Performance     │◀───│ Result Exporter  │◀──────────┘
│   Monitor       │    └──────────────────┘
└─────────────────┘
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- Azure OpenAI API access
- Required packages: `openai`, `pillow`, `pyyaml`, `requests`

### Setup
```bash
# Clone the repository
git clone https://github.com/Ramu-DE/Azure-openAI-Image-Classification.git
cd Azure-openAI-Image-Classification

# Install dependencies
pip install -r requirements.txt

# Configure Azure OpenAI credentials
cp azure.env.example azure.env
# Edit azure.env with your credentials
```

## 🚀 Quick Start

### Single Image Classification
```python
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.core.classifier import ImageClassifier

# Load environment variables
load_dotenv('azure.env')

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize classifier
classifier = ImageClassifier(
    client=client,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)

# Classify a single image
classes = ["dandelion", "rose", "sunflower", "daisy"]
result = classifier.classify_image("flowers_images/class1/dandelion (1).jpg", classes)
print(f"Prediction: {result['prediction']}")
```

### Batch Processing
```python
import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from src.core.classifier import ImageClassifier
from src.batch.processor import BatchProcessor
from src.export.formatters import ResultFormatter

# Load environment variables
load_dotenv('azure.env')

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

# Initialize classifier and batch processor
classifier = ImageClassifier(
    client=client,
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
)
processor = BatchProcessor(classifier, batch_size=10)

# Process directory
classes = ["dandelion", "rose", "sunflower", "daisy"]
results = processor.process_directory("flowers_images/class1", classes)

# Export results
ResultFormatter.to_json(results, "results.json")
ResultFormatter.to_csv(results, "results.csv")
```

### Custom Domain Configuration
```yaml
# config/domains.yaml
flowers:
  classes: [dandelion, rose, sunflower, daisy]
  prompt_template: "Classify this flower image into one of: {classes}"

animals:
  classes: [cat, dog, bird, fish, horse]
  prompt_template: "Identify the animal in this image from: {classes}"
```

## 📁 Project Structure

```
Azure-openAI-Image-Classification/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── classifier.py          # Main classification engine
│   │   ├── preprocessor.py        # Image preprocessing
│   │   ├── validator.py           # Result validation
│   │   └── config_manager.py      # Configuration management
│   ├── batch/
│   │   ├── __init__.py
│   │   ├── processor.py           # Batch processing
│   │   └── progress.py            # Progress tracking
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── performance.py         # Performance monitoring
│   │   └── alerts.py              # Alerting system
│   ├── export/
│   │   ├── __init__.py
│   │   ├── formatters.py          # Export formatters
│   │   └── integrations.py        # External integrations
│   └── utils/
│       ├── __init__.py
│       ├── logging.py             # Logging utilities
│       └── errors.py              # Error handling
├── config/
│   ├── domains.yaml               # Domain configurations
│   ├── settings.yaml              # System settings
│   └── logging.yaml               # Logging configuration
├── tests/
│   ├── unit/                      # Unit tests
│   ├── integration/               # Integration tests
│   └── property/                  # Property-based tests
├── examples/
│   ├── basic_usage.py
│   ├── batch_processing.py
│   └── custom_domain.py
├── docs/
│   ├── api_reference.md
│   ├── configuration.md
│   └── deployment.md
├── flowers_images/                # Dataset (40 images)
│   ├── class1/                    # Dandelion images
│   ├── class2/                    # Rose images
│   ├── class3/                    # Sunflower images
│   └── class4/                    # Daisy images
├── Image classification with Azure OpenAI gpt-4o - Flowers example.ipynb
├── requirements.txt
├── setup.py
├── azure.env.example
├── .gitignore
└── README.md
```

## 🧪 Testing

The system includes comprehensive testing with both unit tests and property-based tests:

```bash
# Run all tests
pytest

# Run property-based tests (100+ iterations each)
pytest tests/property/ -v

# Run performance benchmarks
pytest tests/performance/ --benchmark-only
```

## 📈 Monitoring & Analytics

### Performance Metrics
- Classification accuracy by domain
- Response times and throughput
- API token usage and costs
- Error rates and failure patterns

### Alerting
- Performance degradation alerts
- Cost threshold notifications
- Error rate monitoring
- System health checks

## 🔧 Configuration

### Domain Configuration
```yaml
# config/domains.yaml
domain_name:
  classes: [class1, class2, class3]
  prompt_template: "Custom prompt with {classes}"
  confidence_threshold: 0.7
  max_retries: 3
```

### System Settings
```yaml
# config/settings.yaml
api:
  rate_limit: 60  # requests per minute
  timeout: 30     # seconds
  max_retries: 3

batch:
  default_size: 10
  checkpoint_interval: 100

monitoring:
  enable_metrics: true
  alert_thresholds:
    accuracy: 0.8
    response_time: 5.0
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build image
docker build -t enhanced-image-classifier .

# Run container
docker run -p 8000:8000 -v $(pwd)/config:/app/config enhanced-image-classifier
```

### API Server
```bash
# Start REST API server
python -m src.api.server --port 8000

# Health check
curl http://localhost:8000/health
```

## 📊 Performance Benchmarks

| Metric | Original | Enhanced |
|--------|----------|----------|
| Accuracy | 97% | 97%+ |
| Batch Size | 1 | 10-100 |
| Error Handling | Basic | Comprehensive |
| Monitoring | None | Full Analytics |
| Export Formats | None | JSON/CSV/XML |
| Domains | 1 (Flowers) | Multiple |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Azure OpenAI team for GPT-4o vision capabilities
- Original flower classification notebook as foundation
- Property-based testing methodology for robust validation

## 📞 Support

For questions and support:
- Create an issue in this repository
- Check the [documentation](docs/)
- Review the [examples](examples/)

---

**Built with ❤️ using Azure OpenAI GPT-4o**