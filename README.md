# plyghd Language Server
This project serves as a demonstrator to show how to implement a basic language server that can interface with the [klighd-vscode](https://github.com/kieler/klighd-vscode).
It demonstrates the implementaion of the *DSP* (c.f. [Klighd architectural overview](https://github.com/kieler/klighd-vscode/wiki/Diagram-Server-Communication-%E2%80%90-Architectural-Overview)) in a language that cannot use the Java implementation of the Klighd server.

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
Download the latest version of the [KLighD CLI](https://github.com/kieler/klighd-vscode/releases).
When executing it, the help text provides some usage hints: e.g. `./klighd-linux --help` on Linux systems.

The KLighD CLI usually requests a language server to open the diagram for a specific file. Here we did not implement any model code or loading the file, but we still need a dummy file for this implementation to recognize that it can support a diagram for it. We use the `.kgt` extension. So create a dummy file next to the CLI with the correct extension: `touch dummy.kgt`

Next, launch the CLI and connect it to your language server. Our server uses the default port 5007, so the CLI call looks like this: `./klighd-linux --ls_port 5007 ./dummy.kgt`.

This should open a diagram view in your browser. It will probably not show any diagram yet, because we have to first tell it to use client-layout, which is off by default. To change that option, click on the cogwheel in the browser window (the general options panel of the KLighD CLI), enable the `Render Options>Debug Options` option, scroll to the bottom and enable the `Preferences>Client Layout` option. After this, you will need to restart this plyghd language server and reload the KLighD CLI browser window. A simple diagram with the nodes `nnnn`, `m`, and `o` should be visible in the window now.

To change an option defined by the example synthesis, click on the "options" panel on the right (the sliders icon) and enable/disable the "Lables" option. This is defined and used in the [synthesis.py](https://github.com/kieler/plyghd-ls-demonstrator/blob/main/synthesis.py) file. This follows the message scheme defined in [TODO](https://todo) and implemented in [TODO](https://github.com/kieler/plyghd-ls-demonstrator/blob/main/ls.py)

To perform an action, double click the rectangle behind the `nnnn` node (not the text itself). It will print to the language server console, that the action was performed on the `nnnn` node. This follows the message scheme defined in [TODO](https://todo) and implemented in [TODO](https://github.com/kieler/plyghd-ls-demonstrator/blob/main/ls.py)

## Generating the KGraph data structure from schema
The schema is defined in [klighd-vscode](https://github.com/kieler/klighd-vscode/tree/main/schema/SKGraphSchema.json).

The generated types are committed in this repository. If the schemas are updated they can be rebuilt using the `rebuild_types.sh` build script in the `klighd_types` folder. For this to work the initial setup under getting started has to have been done.
