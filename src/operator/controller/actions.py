import re
from common import hardware
from common.logs import CONTROLLER as logger

def trigger_action(status, alertname):
    try:
        action = '{}_{}'.format(status.lower(), re.sub(r'([A-Z]+)$', r'_\1', alertname).lower())
        logger.debug('Trigger %s action', action)
        eval(action)()
    except Exception as e:
        logger.error('Trigger %s caused error: %s', action, e)

def firing_light_on():
    hardware.LIGHT_RELAY.on()
    logger.info('Toggle LIGHT ON')

def firing_light_off():
    hardware.LIGHT_RELAY.off()
    logger.info('Toggle LIGHT OFF')

def firing_fan_on():
    hardware.FAN_RELAY.on()
    logger.info('Toggle FAN ON')

def firing_fan_off():
    hardware.FAN_RELAY.off()
    logger.info('Toggle FAN OFF')

def firing_water_on():
    hardware.FAN_RELAY.on()
    logger.info('Toggle WATER ON')

def firing_water_off():
    hardware.WATER_RELAY.off()
    logger.info('Toggle WATER OFF')

def firing_temperature_high():
    return

def firing_temperature_low():
    return

def firing_humudity_high():
    return

def firing_humudity_low():
    return

def firing_moisture_high():
    return

def firing_moisture_low():
    return