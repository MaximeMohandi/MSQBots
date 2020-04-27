#!/bin/bash
python3.7 config_file_writer.py
echo "build image"
cd ../..
docker build -t msqbot -f script/deploy/Dockerfile .
docker run -d --name MSQbot --mount source=logs,target=/logs msqbot
echo "done."
