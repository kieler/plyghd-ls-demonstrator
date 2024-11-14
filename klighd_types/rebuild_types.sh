#!/bin/bash
source ../ls-env/bin/activate
git clone git@github.com:kieler/klighd-vscode.git --depth 1
datamodel-codegen --input klighd-vscode/schema/ --input-file-type jsonschema --output . --use-default
rm -rf klighd-vscode/
