@echo off
pip3 install -r requirements.txt
uvicorn backend.main:app
