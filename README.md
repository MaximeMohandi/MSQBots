# MSQBitsReporter2.0
<img src="https://github.com/MaximeMohandi/MSQBitsReporter2.0/blob/master/msqbitsReporter/ressources/reporterLogo.png" width="25%"/>

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

To build the msqbitsreporter image you have to execute the deployReporter.bat file on Windows and the deployReporter.sh file on Linux. these scripts will also create the credentials json files needed to connect to your database and dicord

to run the reporter execute :
```shell
docker -d run msqbitreporter
```

_note: you can check if the bot is running by using_
```docker container ps```

### 🏠 Local Installation
* Pro : You just need python installed
* Cons: You'll have to install all the dependencies and manage eventual compatibility problem and you'll also have to configure a database

_TODO put instruction here_

## Commands List
_TODO put an array with basics command_

## More
_TODO add link to doc_

