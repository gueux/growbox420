from common import config
from common.logs import MAIN as logger
from pigpio_dht import DHT11
from gpiozero import MCP3008, DigitalOutputDevice

try:
	TEMP_HUMD_SENSOR = DHT11(config.DHT11_PIN)
	MOISTURE_SENSOR = MCP3008(channel=config.MCP3008_CHANNEL)
	MOISTURE_SENSOR_POWER = DigitalOutputDevice(config.MCP3008_POWER_PIN)

	FAN_RELAY = DigitalOutputDevice(config.FAN_RELAY_PIN, active_high=False, initial_value=False)
	LIGHT_RELAY = DigitalOutputDevice(config.LIGHT_RELAY_PIN, active_high=False, initial_value=False)
	WATER_RELAY = DigitalOutputDevice(config.WATER_RELAY_PIN, active_high=False, initial_value=False)
except Exception as e:
	logger.error("Hardware doesn't start properly: %s", e)
