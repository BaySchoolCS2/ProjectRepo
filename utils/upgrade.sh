#! /bin/bash

tools-env/bin/pip install --upgrade -r tool-requirements.txt
venv/bin/pip install --upgrade -r requirements.txt

echo "writting packages to files"

tools-env/bin/pip freeze > tool-requirements.txt
venv/bin/pip freeze > requirements.txt

echo "updated all requirements files"
