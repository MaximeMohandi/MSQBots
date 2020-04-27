#!/bin/bash
python3.7 config_file_writer.py
echo "build image"
cd ../..
docker build -t msqbot -f script/deploy/Dockerfile .
docker run -d -it --name MSQbot --volume "$(pwd)"/msqbot_log:/app/msqbot/logs:ro msqbot
echo "done."
