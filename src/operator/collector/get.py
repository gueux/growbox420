import time
from common import config, utils, hardware
from common.metrics import TEMPERATURE, HUMIDITY, MOISTURE, FAN, LIGHT, WATER
from common.logs import COLLECTOR as logger

def all_metrics():

    logger.info("Collecting Metrics for phase: %s", config.CURRENT_PHASE['name'])

    dht11_values()
    #mcp3008_values()
    fan_relay_value()
    light_relay_value()
    water_relay_value()

    logger.info("Collected Metrics for phase: %s", config.CURRENT_PHASE['name'])

def dht11_values():
    # Get DHT11 Temperature & Humidity
    # The parameter is the pin
    logger.info("Get Temperature in C & Humidity from the DHT11 sensor...")
    try:
        result = hardware.TEMP_HUMD_SENSOR.read()

        temp_c = result['temp_c']
        humidity = result['humidity']

        if result['valid']:
            TEMPERATURE.set(temp_c)
            HUMIDITY.set(humidity)
            logger.debug("Temp/Humidity is: %s, %s", temp_c, humidity)

    except Exception as e:
        TEMPERATURE.set(0)
        HUMIDITY.set(0)
        logger.error("Temp/Humid Sensor error: %s", e)

def mcp3008_values():
    #   Get MCP3008 moisture sensor values: 
    #       Values  Condition
    #       --------------------------
    #       0-17    sensor in open air
    #       18-424  sensor in dry soil
    #       425-689 sensor in humid soil
    #       690+    sensor in water
    logger.info("Get Soil Moisture from MCP3008 sensor...")
    # for i in range(8):
    #     sensor = MCP3008(channel=i)
    #     logger.debug("Soil Moisture CHANNEL %s: %s", i, sensor.value)

    try:
        # Sensor is OFF by default in order
        # to minimize corrosion affect
        hardware.MOISTURE_SENSOR_POWER.on()
        time.sleep(2)
        sensor_values = []
        # 10 readings 10 milliseconds apart
        for i in range(10):
            time.sleep(.01)
            sensor_values.append(hardware.MOISTURE_SENSOR.value)
        logger.debug("Soil Moisture values is: %s",sensor_values)
        moisture = utils.moisture_calibrate(sensor_values)

        hardware.MOISTURE_SENSOR_POWER.off()

        if moisture:
            MOISTURE.set(moisture)
            logger.debug("Soil Moisture is: %s", moisture)
    except Exception as e:
        logger.error("Moisture Sensor error: %s", e)

def fan_relay_value():
    logger.info("Fan Relay get status...")
    try:
        status = hardware.FAN_RELAY.value
        FAN.set(status)
        logger.debug("Fan Relay status is: %s", config.RELAY_MODES[status])
    except Exception as e:
        FAN.set(-1)
        logger.error("Get Fan Relay error: %s", e)

def light_relay_value():
    logger.info("Light Relay get status...")
    try:
        status = hardware.LIGHT_RELAY.value
        LIGHT.set(status)
        logger.debug("Light Relay status is: %s", config.RELAY_MODES[status])
    except Exception as e:
        LIGHT.set(-1)
        logger.error("Get Light Relay error: %s", e)

def water_relay_value():
    logger.info("Water Relay get status...")
    try:
        status = hardware.WATER_RELAY.value
        WATER.set(status)
        logger.debug("Water Relay status is: %s", config.RELAY_MODES[status])
    except Exception as e:
        WATER.set(-1)
        logger.error("Get Water Relay error: %s", e)