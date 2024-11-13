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
python ls.py --port 5007
```

## Connecting with a client
The simplest way to use the demonstrator is to use the [klighd-cli](https://github.com/kieler/klighd-vscode/releases). Version 0.6.0 and onwards support client-only layout.

To connect to the running server (use appropriate executable for your OS):
```
klighd-linux --ls_port 5007 ./empty.kgt
```
The klighd-cli expects always expects a file, but this example server doesn't actually need one so we just pass an empty `kgt` file.

By default the klighd-cli assumes that the server can perform layout.
We need to change this:
1. Open the sidebar
2. Enable Debug Options
3. Scroll down to the bottom and Enable Client Layout

This setting is now cached and when the server is restarted the setting will persist.

## Generating the KGraph data structure from schema
Schema in [klighd-vscode](https://github.com/kieler/klighd-vscode/tree/main/schema/SKGraphSchema.json)
```
datamodel-codegen --input SKGraphSchema.json --input-file-type jsonschema --output skgraph.py
```