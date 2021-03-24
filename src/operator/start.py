########
# GreenLab controller
# Version: 0.0.1 (This is a working BETA vesion)
# Ihor Savchenko
#
# This project is released under The MIT License (MIT)
# Copyright 2020 Ihor Savchenko
########

########
# Code is compatible with Python 2.7 and Python 3.5.
# !/usr/bin/env python
# coding=utf-8
########

########
# python module that recieve alers from Alertmanager and start/stop GreenLab actions
########
import time
import datetime
import argparse
import threading
from common import config
from common.logs import MAIN as logger
from models.lifecycle import LIFECYCLE
from collector.phases import current_phase
from collector.get import all_metrics
from controller.routes import app

def controller():
    logger.info("Starting Flask HTTP server...")
    app.run(host=config.FLASK_HOST, port=config.FLASK_PORT, debug=True, use_reloader=False)

def collector():
    while True:
        logger.info("Calculate current phase and time of the day...")
        config.CURRENT_PHASE = current_phase(LIFECYCLE, startup_date_time)
        logger.info("Collecting current metrics...")
        all_metrics()
        logger.info("Metrics Collected. Sleep for %s sec...", config.READ_EVERY_SEC)
        time.sleep(config.READ_EVERY_SEC)

if __name__ == "__main__":

     # Moment when the growcycle was started
     
    startup_date_time = datetime.datetime.now()

    logger.info("====================================")
    logger.info("Startup Date/Time: %s", startup_date_time.strftime("%y-%m-%d %H:%M:%S"))
    logger.info("====================================")
    logger.info("Controller starting in separate thread...")
    logger.info("====================================")
    
    threading.Thread(target=controller).start()

    logger.info("====================================")
    logger.info("Collector starting in separate thread...")
    logger.info("====================================")
    
    threading.Thread(target=collector).start()