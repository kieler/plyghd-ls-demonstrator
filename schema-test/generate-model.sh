for s in /home/mka/projects/keith/klighd-vscode/schema/*/*.json ; do datamodel-codegen --input "$s" --input-file-type jsonschema --output "$(basename "$s" .json).py" ; done
