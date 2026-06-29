# frankfurter-api - Simple Wrapper for the Fankfurter Currency API


![PyPI Downloads](https://img.shields.io/pypi/dm/frankfurter-api)
![PyPI Version](https://img.shields.io/pypi/v/frankfurter-api)
![PyPI License](https://img.shields.io/pypi/l/frankfurter-api)

# Installation 

```bash
pip install frankfurter-api
```
or
```bash
uv add frankfurter-api
```

# Usage

```py
from frankfurter-api import FrankfurterAPI

frankfurter = FrankfurterAPI()

currencies = await frankfurter.get_currencies()
rate = await frankfurter.get_rate(base="EUR", target="USD")
```

# API Documentation

For more details on the Frankfurter API, visit their official [Documentation](https://www.frankfurter.dev/).

