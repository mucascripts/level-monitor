#!/usr/bin/env bash

set -e
set -x

python -m pip install --upgrade pip
pip install --upgrade pip-tools
pip-compile --upgrade --resolver=backtracking --strip-extras requirements/requirements-dev.in
