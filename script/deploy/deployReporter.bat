@Echo off
python config_file_writer.py

Echo "build image"

cd ../..

docker build -t msqbot -f %~dp0../deploy/Dockerfile .

ECHO "run container as service"

docker run -d --name MSQbot -v ./msqbot_logs:/app/logs msqbot

ECHO "Done."

