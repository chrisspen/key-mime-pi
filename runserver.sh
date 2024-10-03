#!/bin/bash
. .env/bin/activate
DEBUG=1 PORT=8000 ./app/main.py
