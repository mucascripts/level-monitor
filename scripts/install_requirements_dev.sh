#!/usr/bin/env bash

set -e
set -x

python -m pip install --upgrade pip
pip install -r requirements/requirements-dev.txt
