## Venv
```
python -m venv .venv  
.venv\Scripts\Activate.ps1
```

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
