@Echo off
python config_file_writer.py
Echo "build image"
cd ../..
docker build -t msqbot -f %~dp0../deploy/Dockerfile .

docker run -d -it --name MSQbot --volume $pwd/msqbot_log:/app/msqbot/logs:ro msqbot
Echo done.