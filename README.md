# MSQBitsReporter2.0
<img src="https://github.com/MaximeMohandi/MSQBitsReporter2.0/blob/master/msqbitsReporter/resources/reporterLogo.png" width="25%"/>

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

The first vesrion of this bot has been developed as a pratical project to train my python skills. However, sometimes I thaught of new features and here we are.

## ✨Features
*This bot is entirely modulable, this main features has been design for my usage but I developped it to be easly adapted.* 

* Display RSS feed articles
* Display timetable planning from school API
* Discord Bot API

## 🖥 Environment Support

| [<img src="https://upload.wikimedia.org/wikipedia/commons/archive/a/a3/20150828174227%21Windows10Logo.png" width="24px" height="24px"/>](https://www.microsoft.com/fr-fr/windows)</br> Windows | [<img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Ubuntu_and_Ubuntu_Server_Icon.png" width="24px" heigth="24px"/>](https://ubuntu.com/)<br/> Ubuntu |
| ------ | ----------- |
| 8, 10   | 16.04 LTS to 18.04 LTS |
## 📦 Installation


### 🐳 Docker Installation
* Pro : Can be installed on any machines with a minimum configuration
* Cons: You'll have to install Docker. Refere to [this](https://docs.docker.com/install/) official documentation to install docker

To build the msqbitsreporter image you have to execute the [deployReporter.bat](https://github.com/MaximeMohandi/MSQBitsReporter2.0/blob/master/script/deploy/deployReporter.bat) file on Windows and the [deployReporter.sh](https://github.com/MaximeMohandi/MSQBitsReporter2.0/blob/master/script/deploy/deployMsqbitreporter.sh) file on Linux. these scripts will also create the credentials json files needed to connect to your database and dicord


to run the reporter with docker, first clone this repo then go to script/deploy and execute the script corresponding to your OS

with linux:
```shell
sudo bash deployReporter.sh
```
with windows: execute the .bat file

Then run the images with:
```shell
docker -d run msqbitreporter
```

_note: you can check if the bot is running by using_
```docker container ps```

### 🏠 Local Installation
* Pro : You just need python installed
* Cons: You'll have to install all the dependencies on your system and manage the path problem

To write the conf file you can execute the config_file_writer.py or write a config.ini file in msqbitsReporter/resources

## Commands List
_all the commands have to get prefixed ex:  ```$help``` to get the command list_

There's 2 type of command for now:

* news

| commands  | result |
| ------------- | ------------- |
| getnews  | Display last four articles for each newspapers saved in database  |
| getnewspapers | Display a list of all the saved newspapers | 
| getcategories | Display a list of all news categories saved | 
| getnewsby | Display a list of all news by selected category | 
| getnewsfrom |  Display articles from a selected newspaper |
| addnewspaper | Add a new newspaper |
| removenewspaper | Remove a newspaper |

* Planning

| commands  | result |
| ------------- | ------------- |
| edt | Display planed course |
| daycourse | Display planed course for given day |
| todayedt | display course scheduled today |
| nextroom | give next classroom |

## More
_TODO add link to doc_

