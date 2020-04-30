#!/bin/bash
python3.7 config_file_writer.py
echo "build image"
cd ../..
docker build -t msqbot -f script/deploy/Dockerfile .

echo "run container as service"

docker run -d --name MSQbot -v ./msqbot_logs:/app/logs:ro msqbot

echo "done."
