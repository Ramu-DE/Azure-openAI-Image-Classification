# Configuration Guide

## Domain Configuration

Configure classification domains in `config/domains.yaml`:

```yaml
flowers:
  classes:
    - dandelion
    - rose
    - sunflower
    - daisy
  prompt_template: "Classify this flower image into one of: {classes}"
  confidence_threshold: 0.7
```

## System Settings

Configure system behavior in `config/settings.yaml`:

```yaml
api:
  rate_limit: 60
  timeout: 30
  max_retries: 3

batch:
  default_size: 10
  checkpoint_interval: 100
```

## Environment Variables

Create `azure.env` file with your Azure OpenAI credentials:

```
AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
```

## Logging Configuration

Configure logging in `config/logging.yaml`:

```yaml
version: 1
handlers:
  console:
    class: logging.StreamHandler
    level: INFO
```
