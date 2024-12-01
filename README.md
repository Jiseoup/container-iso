# Container ISO
A Python package based on ISO 6346 Container Codes.  
This package provides functionalities to search for container information using ISO codes and to validate container numbers.

## Installation
Install the package using pip:
```bash
pip install container-iso
```

## Dataset
The dataset used in this package is derived from the [ISO-Container-Codes](https://github.com/datasets/ISO-Container-Codes) repository, processed to enhance usability.

## Usage
### Search Container Information
You can retrieve detailed container information using an ISO code:
```python
from container_iso import get_container_info

# Example usage
container_info = get_container_info.get('22GP')
print(container_info)
```

### Validate Container Numbers
Validate whether a container number is compliant with the ISO 6346 standard:

```python
from container_iso import validate_container

# Example usage
is_valid = validate_container('MSCU1234567')
print('Valid Container Number' if is_valid else 'Invalid Container Number')
```

## License

This project is licensed under the MIT License.
