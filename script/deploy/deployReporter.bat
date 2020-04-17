@Echo off
python config_file_writer.py
Echo "build image"
cd ../..
docker build -t msqbot -f %~dp0../deploy/Dockerfile .

docker run --name MSQbot -d msqbot
Echo done.