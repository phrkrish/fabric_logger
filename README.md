# Fabric Logger

Fabric Logger is a simple Python logger designed for use with Fabric. It provides an easy-to-use interface for logging messages in your Fabric scripts, making it easier to track and debug your automation tasks.

## Features

- Simple and easy-to-use logging interface
- Supports multiple log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Customizable log format
- Console and file logging

## Installation

To install Fabric Logger, use pip:

```sh
pip install fabric_logger
```

## Usage
Here is a basic example of how to use Fabric Logger in your Fabric script:
```python
from fabric import task
from fabric_logger import get_logger

# Initialize the logger
logger = get_logger('fabric_logger')

@task
def deploy(c):
    logger.info("Starting deployment")
    try:
        # Your deployment code here
        logger.info("Deployment successful")
    except Exception as e:
        logger.error(f"Deployment failed: {e}")
```

## Configuration
You can configure the logger by passing arguments to the get_logger function. For example:

```python
logger = get_logger(
    name='fabric_logger',
    log_file='fabric.log',
    log_level='DEBUG',
    log_format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

## Development
To set up the development environment:

Clone the repository:
```sh
git clone https://github.com/yourusername/fabric_logger.git
cd fabric_logger
```

Create a virtual environment and activate it:
```sh
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
Install the dependencies:
```sh
pip install -r requirements.txt
```
Run the tests:
```sh
pytest
```
Issues
While creating this package, I faced two issues:

Module Not Found:

If you encounter an error like ModuleNotFoundError: No module named 'setuptools', you need to install the setuptools package by running: pip install setuptools.
Module Not Found While Testing the Implementation:

To resolve the issue of modules not being found during testing, add the package to the system path with the following code:
```python
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```