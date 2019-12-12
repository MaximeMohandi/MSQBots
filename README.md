# MSQBotsReporter
<img src="https://github.com/MaximeMohandi/MSQBitsReporter2.0/blob/master/msqbitsReporter/resources/reporterLogo.png" width="25%"/>

[![License: MPL 2.0](https://img.shields.io/badge/License-MPL%202.0-brightgreen.svg)](https://opensource.org/licenses/MPL-2.0)

This has been originally developed as a practical project to train my python's skills. However, sometimes with time I added some features
and now I thaught I could just share it.

The bot is entirely developed in Python with Discord.py.

## Features
*I tried to make this bot modular but it need some improvements. In particular for the school API* 

* Display RSS feed articles
* Display timetable planning from school API
* Discord Bot API

## Environment Support

| [<img src="https://upload.wikimedia.org/wikipedia/commons/archive/a/a3/20150828174227%21Windows10Logo.png" width="24px" height="24px"/>](https://www.microsoft.com/fr-fr/windows)</br> Windows | [<img src="https://upload.wikimedia.org/wikipedia/commons/1/16/Ubuntu_and_Ubuntu_Server_Icon.png" width="24px" heigth="24px"/>](https://ubuntu.com/)<br/> Ubuntu |
| ------ | ----------- |
| 8, 10   | 16.04 LTS to 18.04 LTS |


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


