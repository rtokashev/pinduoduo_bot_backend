#!/bin/sh

PYTHONPATH=src alembic upgrade head
python3 src/main.py
