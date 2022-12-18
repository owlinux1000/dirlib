# dirlib

`dirlib` is a minimum library for getting a directory that is used by putting on configuration files. This is inspired by Golang standard library function called `os.UserConfigDir()`. Currently, Windows, Unix and macOS are supported.

## Installation

```
pip install dirlib
```

## How to use

```
import dirlib
print(dirlib.user_config_dir())
```