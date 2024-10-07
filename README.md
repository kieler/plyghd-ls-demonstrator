# plyghd Language Server
This project serves as a demonstrator to show how to implement a basic language server that can interface with the [klighd-vscode](https://github.com/kieler/klighd-vscode)

## Getting Started
Setup a virtual environment and install the required packages.
```
python -m venv ls-env
source ls-env/bin/activate
pip install -r requirements.txt
```
Launch the python language server
```
python ls.py
```

## Connecting with a client
TODO: how to start klighd-cli

## Generating the KGraph data structure from schema
```
datamodel-codegen --input SKGraphSchema.json --input-file-type jsonschema --output skgraph.py
```