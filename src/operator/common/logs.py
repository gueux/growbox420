import sys
import logging

LOG_LEVEL = logging.DEBUG

MAIN = logging.getLogger('main')
CONTROLLER = logging.getLogger('controller')
COLLECTOR = logging.getLogger('collector')

for l in [MAIN, CONTROLLER, COLLECTOR]:
    l.setLevel(LOG_LEVEL)
    #fh = logging.FileHandler(LOG_DIR + l.name + '.log')
    sh = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #fh.setFormatter(formatter)
    sh.setFormatter(formatter)
    # l.addHandler(fh)
    l.addHandler(sh)