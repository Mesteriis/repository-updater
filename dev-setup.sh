#!/bin/sh

pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt
pip3 install --user -r requirements-dev.txt
pre-commit install
pre-commit autoupdate
