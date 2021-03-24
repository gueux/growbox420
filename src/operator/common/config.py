import os
import yaml
from common.logs import MAIN as logger

VERSION = '0.0.1'

PLANT = os.environ.get('PLANT') or 'microgreen'

READ_EVERY_SEC = os.environ.get('READ_EVERY_SEC') or 15

CURRENT_PHASE = {}
LIGHT_DARK_MODES = ['Day', 'Night']
RELAY_MODES = ['OFF', 'ON']

DHT11_PIN = os.environ.get('DHT11_PIN') or 4

MCP3008_CHANNEL=0
MCP3008_POWER_PIN=17


LIGHT_RELAY_PIN = os.environ.get('LIGHT_RELAY_PIN') or 14 # RELAY 1
FAN_RELAY_PIN = os.environ.get('FAN_RELAY_PIN') or 15   # RELAY 2
WATER_RELAY_PIN = os.environ.get('WATER_RELAY_PIN') or 18 # RELAY 3


FLASK_HOST = os.environ.get('FLASK_HOST') or '0.0.0.0'
FLASK_PORT = os.environ.get('FLASK_PORT') or 5000

ALERTS = {
  "LightON": 0,
  "LightOFF": 0,
  "TemperatureLOW": 0,
  "TemperatureHIGH": 0,
  "HumudityLOW": 0,
  "HumudityHIGH": 0,
  "MoistureLOW": 0,
  "MoistureHIGH": 0,
  "InstanceDown": 0,
}

# The script will use folders inside `DATA_PATH` path as `database` in rethinkdb 
# We'll create the table for every yaml file inside abovementioned folder

DATA_PATH = os.environ.get('DATA_PATH') or './models/data'

#### RethinkDB Connection details

RDB_HOST =  os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015
