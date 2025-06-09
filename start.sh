#!/bin/bash
pip install -r requirements.txt
exec python3 -m uvicorn main:app --host 0.0.0.0 --port $PORT