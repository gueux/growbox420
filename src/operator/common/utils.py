import re
import yaml
import datetime
from common.logs import MAIN as logger

PHASE_REGEX = re.compile(r'((?P<days>\d+?)d)?((?P<hours>\d+?)h)?((?P<minutes>\d+?)m)?((?P<seconds>\d+?)s)?')

def parse_time(time_str):
    parts = PHASE_REGEX.match(time_str)
    if not parts:
        return
    parts = parts.groupdict()
    time_params = {}
    for (name, param) in parts.items():
        if param:
            time_params[name] = int(param)
    return datetime.timedelta(**time_params)

def moisture_calibrate(values):
    values.sort()
    return values[len(values)//2]

def read_yaml(file):
    with open(file, "r") as f:
        logger.debug("Loading file: %s", file)
        yaml_file = yaml.full_load(f)
        logger.debug("Loaded file: %s", yaml_file)
        return yaml_file