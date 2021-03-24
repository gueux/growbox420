from common.config import LIGHT_DARK_MODES, VERSION
from common.logs import MAIN as logger
from models.lifecycle import LIFECYCLE
from prometheus_client import Info, Gauge, Enum

phases = []
for phase in LIFECYCLE:
    phases.append(phase['name'])

try:

    BUILD = Info('growbox_build', 'Growbox Automation Platform', ['version'])
    BUILD.labels(version=VERSION)

    PHASE_NAME = Enum('growbox_phase_name', 'Growbox Current Phase name', states=phases)

    PHASE_DURATION = Gauge('growbox_phase_duration_seconds', 'Growbox Current Phase duration')
    PHASE_FROM_START = Gauge('growbox_phase_from_start_seconds', 'Growbox Current Phase seconds from start')
    PHASE_BEFORE_FINISH = Gauge('growbox_phase_before_finish_seconds', 'Growbox Current Phase seconds before finish')

    LIGHT_DARK_MODE = Enum('growbox_light_dark_mode', 'Current Growbox Light/Dark mode', states=LIGHT_DARK_MODES)
    LIGHT_DARK_MODE_DURATION = Gauge('growbox_light_dark_mode_duration_seconds', 'Growbox Current Light/Dark mode duration')
    LIGHT_DARK_MODE_FROM_START = Gauge('growbox_light_dark_mode_from_start_seconds', 'Growbox Current Light/Dark mode seconds from start')
    LIGHT_DARK_MODE_BEFORE_FINISH = Gauge('growbox_light_dark_mode_before_finish_seconds', 'Growbox Current Light/Dark mode seconds before finish')

    FAN = Gauge('growbox_fan_enabled', 'Growbox FANNING enabled')
    LIGHT = Gauge('growbox_light_enabled', 'Growbox LIGHTENING enabled')
    WATER = Gauge('growbox_water_enabled', 'Growbox WATERING enabled')

    TEMPERATURE = Gauge('growbox_temperature_celsius', 'Growbox Temperature')
    HUMIDITY = Gauge('growbox_humidity_percents', 'Growbox Humidity')
    MOISTURE = Gauge('growbox_moisture_percents', 'Growbox Moisture')

except ValueError as e:
    logger.error("Prometheus Metrics are not properly initialized")
    logger.debug(e)
    exit()