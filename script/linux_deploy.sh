#!/bin/sh

REPO_SRC=https://github.com/MaximeMohandi/MSQBotsReporter.git
LOCAL_REPO=MSQBots
VENV_NAME="env"
CONFIG_WRITER_PATH="script/config_file_writer.py"
PID_FILE=msqbotPID.txt

# return to root
cd ../..

# clone or pull sources from given repos
clone_or_pull_reporter () {
	if [ ! -d $LOCAL_REPO ]
	then
		echo 'repo does not exist. Cloning ...'
		git clone $REPO_SRC
		cd $LOCAL_REPO
	else
		echo 'repo already exist. Pull...'
		cd $LOCAL_REPO
		git pull
	fi
}

# create virtual environment if doesn't exist
set_virtual_env () {
	if [ ! -d $VENV_NAME ]
	then
		echo 'create virtual env'
		python3.8 -m venv $VENV_NAME
	fi
}

# run reporter configurer
write_reporter_config_if_not_exist () {
	if [ -d msqbot ]
	then
		echo 'configure bot'
		$VENV_NAME/bin/python $CONFIG_WRITER_PATH
	fi
}

#launch msqbot in background
start_reporter () {
	if [ -f $PID_FILE ]
	then
		kill -9 `cat $PID_FILE`
	fi
	nohup $VENV_NAME/bin/python -m msqbot > my.log 2>&1 &
	echo $! > $PID_FILE
	echo 'reporter running'
}

clone_or_pull_reporter
set_virtual_env

echo 'get dependencies changes'
$VENV_NAME/bin/pip install -r requirements.txt

write_reporter_config_if_not_exist
start_reporter
