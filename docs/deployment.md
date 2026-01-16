# Deployment Guide

## Prerequisites

- Python 3.8+
- Azure OpenAI API access
- Required packages installed

## Installation

```bash
# Clone repository
git clone https://github.com/Ramu-DE/Azure-openAI-Image-Classification.git
cd Azure-openAI-Image-Classification

# Install dependencies
pip install -r requirements.txt

# Configure credentials
cp azure.env.example azure.env
# Edit azure.env with your credentials
```

## Running the Application

### Single Image Classification

```bash
python examples/basic_usage.py
```

### Batch Processing

```bash
python examples/batch_processing.py
```

### Custom Domain

```bash
python examples/custom_domain.py
```

## Docker Deployment

```bash
# Build image
docker build -t image-classifier .

# Run container
docker run -p 8000:8000 -v $(pwd)/config:/app/config image-classifier
```

## Production Considerations

- Set appropriate rate limits
- Configure monitoring and alerting
- Use environment-specific configurations
- Enable logging for troubleshooting
- Implement backup and recovery procedures
