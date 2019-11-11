import schedule
import time
from threading import Thread


def __schedule_sender():
    print('sheduled')
    schedule.every(1).minutes.do(send_news)
    """schedule.every().hour.do(job)
    schedule.every().day.at("10:30").do(job)
    schedule.every(5).to(10).minutes.do(job)
    schedule.every().monday.do(job)
    schedule.every().wednesday.at("13:15").do(job)
    schedule.every().minute.at(":17").do(job)"""
    while True:
        schedule.run_pending()
        time.sleep(1)


def send_news():
    print('sended')


def run():
    Thread(target=__schedule_sender).start()


run()