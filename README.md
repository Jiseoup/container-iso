# ISO Container
A Python package based on ISO 6346 Container Codes.  
This package provides functionalities to search for container information using ISO codes and to validate container numbers.

## Installation
Install the package using pip:
```bash
pip install iso-container
```

## Usage
### Search Container Information
You can retrieve detailed container information using an ISO code:
```python
from iso_container import get_container_info

# Example usage
container_info = get_container_info('22GP')
print(container_info)
```

### Validate Container Numbers
Validate whether a container number is compliant with the ISO 6346 standard:

```python
from iso_container import validate_container

# Example usage
is_valid = validate_container('MSCU1234567')
print('Valid Container Number' if is_valid else 'Invalid Container Number')
```

## Dataset
The dataset used in this package is derived from the [ISO-Container-Codes](https://github.com/datasets/ISO-Container-Codes) repository, processed to enhance usability.

## License
This project is licensed under the [MIT License](https://github.com/Jiseoup/container-iso/blob/main/LICENSE).
