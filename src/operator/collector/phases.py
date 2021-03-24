import datetime
from .day import current_light_dark_mode
from common import config
from common.logs import COLLECTOR as logger
from common.utils import parse_time
from common.metrics import PHASE_NAME, PHASE_DURATION, PHASE_FROM_START, PHASE_BEFORE_FINISH

def calculate_phases_timedelta(lifecycle=[]):
    timedelta = []
    for index, phase in enumerate(lifecycle):
        if index == 0:
            timedelta.append(parse_time(phase['duration']))
        else:
            timedelta.append(parse_time(phase['duration']) + timedelta[index - 1])
    return timedelta

def current_phase_index(phases_timedelta, uptime):
    for index, timedelta in enumerate(phases_timedelta):
        if index == 0 and uptime <= timedelta:
            logger.debug("Current uptime %s <= %s", uptime, timedelta)
            return 0
        elif uptime > phases_timedelta[index - 1] and uptime <= timedelta:
            logger.debug("Current uptime %s > %s AND <= %s", uptime, phases_timedelta[index - 1], timedelta)
            return index
            break
        elif uptime > phases_timedelta[-1]:
            raise RuntimeError("we are out of lifecycle!!!")
        else:
            logger.debug("Its not phase %s. Check next", index)

def current_phase_metrics(timedelta, index, uptime, duration):
    PHASE_DURATION.set(parse_time(duration).seconds)
    logger.debug("Current Phase Duration: %s", int(PHASE_DURATION._value.get()))
    if index == 0:
        PHASE_FROM_START.set(uptime.seconds)
    else:
        PHASE_FROM_START.set((uptime - timedelta[index - 1]).seconds)
    logger.debug("Time from Phase start: %s", PHASE_FROM_START._value.get())
    PHASE_BEFORE_FINISH.set((timedelta[index] - uptime).seconds)
    logger.debug("Time before Phase finish: %s", PHASE_BEFORE_FINISH._value.get())

def current_phase(lifecycle, startup_date_time):
    try:
        # Get current date & times
        current_date_time = datetime.datetime.now()
        logger.info("Current Date/Time is %s", current_date_time.strftime("%y-%m-%d %H:%M:%S"))
        current_uptime = current_date_time - startup_date_time
        logger.debug("Current Uptime: %s", current_uptime)

        # Calculate Phases timedelta
        phases_timedelta = calculate_phases_timedelta(lifecycle)
        
        logger.debug("Phases Timedeltas: %s", phases_timedelta)

        # Check which phase we are currently in
        current_index = current_phase_index(phases_timedelta, current_uptime)
        current_phase = lifecycle[current_index]

        logger.debug("Current Phase config:")
        for key, value in current_phase.items():
            logger.debug("%s: %s", key, value)

        PHASE_NAME.state(current_phase['name'])
        current_phase_metrics(phases_timedelta, current_index, current_uptime, current_phase['duration'])
        current_light_dark_mode(current_phase)
        return current_phase

    except Exception as e:
        logger.debug("Error defining current lifecycle phase: %s", e)