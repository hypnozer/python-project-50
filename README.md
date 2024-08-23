
[![Actions Status](https://github.com/hypnozer/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/hypnozer/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/37bda12bb9602a92da94/maintainability)](https://codeclimate.com/github/hypnozer/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/37bda12bb9602a92da94/test_coverage)](https://codeclimate.com/github/hypnozer/python-project-50/test_coverage)

# Difference Calculator

Difference Calculator is a program that determines the difference between two data structures. This is a common task for which there are many online services, such as jsondiff. A similar mechanism is used, for example, when displaying test results or automatically tracking changes in configuration files.

## Features

- Support for different input formats: YAML, JSON
- Report generation in plain text, stylish, and JSON formats

Usage Example
To compare two files and generate a report in plain text format, use the following command:

```gendiff --format plain filepath1.json filepath2.yml```

Example Output
```Setting "common.setting4" was added with value: False```
```Setting "group1.baz" was updated. From 'bas' to 'bars'```
```Section "group2" was removed```

Installation
To install the Difference Calculator, follow these steps:

Clone the repository:
```git clone https://github.com/yourusername/difference-calculator.git```

Navigate to the project directory:
```cd difference-calculator```

Install the dependencies:
```npm install```

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.


Feel free to customize it further to fit your project's needs! If you have any other questions or need more help, just let me know. 😊
