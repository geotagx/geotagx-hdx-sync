#!/bin/bash

#
# Creating a virtual environment.
#
virtualenv venv

#
# Installing dependencies
#
source venv/bin/activate
pip install -r requirements.txt
