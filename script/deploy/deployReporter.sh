#!/bin/bash
python3.7 config_file_writer.py
echo "build image"
cd ../..
docker build -t msqbitreporter -f script/deploy/Dockerfile .
docker run --name MSQbot -d msqbot
echo "done."
