"""Setup configuration for the package"""

from setuptools import setup, find_packages

setup(
    name="azure-openai-image-classification",
    version="1.0.0",
    description="Enhanced Image Classification Pipeline with Azure OpenAI GPT-4o",
    author="Ramu-DE",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "pillow>=10.0.0",
        "pyyaml>=6.0",
        "requests>=2.31.0",
        "python-dotenv>=1.0.0"
    ],
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
