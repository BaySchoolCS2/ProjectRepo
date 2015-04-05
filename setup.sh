#! /bin/bash
virtualenv venv
virtualenv tools-env

tools-env/bin/pip install -r tool-requirements.txt
venv/bin/pip install -r requirements.txt

echo "done with setup"
