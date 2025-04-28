
## Install Poetry
Install Poetry (user-local, recommended):
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

Initialize Poetry in your project folder:
```
poetry init
```
Install dependencies:
```
poetry install
```

## Azure Functions Core Tools
```
npm install -g azure-functions-core-tools@4 --unsafe-perm true
func --version
func start
```

### func start:

1. It loads your Azure Functions project
2. Starts a local web server (usually on port 7071)
3. Initializes your function triggers
4. Makes your HTTP endpoints available for local testing
5. Sets up local debugging capabilities

**How it works**
1. **Project Discovery**: The command scans your project directory for function.json files or function decorators (in Python/C#) to identify all functions
2. **Environment Setup**: It loads environment variables from local.settings.json
3. **Runtime Initialization**: Starts the appropriate language runtime (Python in your case)
4. **Trigger Registration**: Sets up listeners for triggers (HTTP, timer, etc.)
5. **Output**: Shows function URLs and logs function executions in real-time

Command options
Some useful options include:
```
func start --verbose       # Show detailed logs
func start --port 9000     # Use a specific port
func start --debug         # Enable debugging
func start --cors *        # Enable CORS for all origins
```

## Python verion
Azure Functions requires Python 3.6.x to 3.11.x
Shows available versions:
```
py -0
```
### venv

Then, create the virtual environment with your chosen version. For example, to use Python 3.11:
```
py -3.11 -m venv .venv311
.venv311\Scripts\Activate.ps1
```

### Reinstall dependencies
```
poetry env use .venv311\Scripts\python.exe # needs only once
poetry install
```

Check `venv` with Poetry:
```
poetry env info
```