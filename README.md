# ML API

This is our ML API

## Requirements

1. Python 3.12.0
2. Pip 23.2.1
3. Make (preferred)

## How to run

1. Run below command to install all dependencies

```sh
pip install -r requirements.txt
```

2. To run the application in development mode, you can run below command:

```sh
make dev

# Or you can run with below command
uvicorn --app-dir src main:app --reload
```

3. To run the appliaction in production mode, you can run below command:

```sh
make start

# Or you can run with below command
uvicorn --app-dir src main:app
```
