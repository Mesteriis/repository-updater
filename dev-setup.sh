#!/bin/sh

pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt -r requirements-dev.txt -r requirements-tests.txt
pre-commit install
pre-commit autoupdate
