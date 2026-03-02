#!/bin/bash
git clone https://github.com/kieler/klighd-vscode.git --depth 1
datamodel-codegen --input klighd-vscode/schema/ --input-file-type jsonschema --output-model-type pydantic_v2.BaseModel --output ./src/kieler_klighd_types --use-default
rm -rf klighd-vscode/
