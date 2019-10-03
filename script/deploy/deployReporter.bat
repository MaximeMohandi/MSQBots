@Echo off
python config_file_writer.py
Echo "build image"
cd ../..
docker build -t msqbitreporter -f %~dp0../deploy/Dockerfile .
Echo done.