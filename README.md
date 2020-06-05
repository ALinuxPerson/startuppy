# startuppy

Startuppy is a Python script and library that implements a cross platform way of adding commands to startup.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install startuppy.

```bash
pip install startuppy
```

## Usage

### Library
```python
import startuppy

command: str = "/usr/bin/ls"  # insert your command here
startup: startuppy.Startup = startuppy.Startup(command)

# to add things to startup
startup.add()

# to remove things (created by startuppy) from startup
startup.remove()

```
### Script
```bash
startuppy --add /usr/bin/ls  # to add things to startup

startuppy --remove /usr/bin/ls  # To remove things (created by startuppy) from startup

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)