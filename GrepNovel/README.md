
## Setup Linter and formatter

Install pylint and black

```
pyenv exec python -m pip install -U pylint
pyenv exec python -m pip install -U black
```

Add these lines to vscode setting.json

```json
"python.linting.pylintEnabled": true,
"python.linting.enabled": true,
"python.formatting.provider": "black",
```

## Install Modules

Run command in cs folder

```
python -m pip install -r requirements.txt
```

## Run Test

```
python -m unittest
```
