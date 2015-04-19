#! /bin/bash

tools-env/bin/pip install --upgrade -r tool-requirements.txt
venv/bin/pip install --upgrade -r requirements.txt

tools-env/bin/pip freeze > tool-requirements.txt
venv/bin/pip freeze > requirements.txt

echo "updated all requirements"
