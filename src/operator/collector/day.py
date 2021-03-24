import datetime
from common.utils import parse_time
from common.logs import COLLECTOR as logger
from common.config import LIGHT_DARK_MODES
from common.metrics import PHASE_DURATION, PHASE_FROM_START, PHASE_BEFORE_FINISH, LIGHT_DARK_MODE, LIGHT_DARK_MODE_DURATION, LIGHT_DARK_MODE_FROM_START, LIGHT_DARK_MODE_BEFORE_FINISH

# def current_light_dark_mode_metrics(timedelta, index, uptime, duration):
#     PHASE_DURATION.set(parse_time(duration).seconds)
#     logger.debug("Current Phase Duration: %s", int(PHASE_DURATION._value.get()))
#     if index == 0:
#         PHASE_FROM_START.set(uptime.seconds)
#     else:
#         PHASE_FROM_START.set((uptime - timedelta[index - 1]).seconds)
#     logger.debug("Time from Phase start: %s", PHASE_FROM_START._value.get())
#     PHASE_BEFORE_FINISH.set((timedelta[index] - uptime).seconds)
#     logger.debug("Time before Phase finish: %s", PHASE_BEFORE_FINISH._value.get())

def current_light_dark_mode(phase):
    current_mode = ''
    try:
        logger.info("Phase Light/Dark mode is: %s", phase['light_dark_mode'])
        light_period, dark_period = map(parse_time, phase['light_dark_mode'].split('/'))

        # Start checking from 0 second in every phase
        timedelta = datetime.timedelta(seconds=0)
        current_phase_duration = datetime.timedelta(seconds=int(PHASE_DURATION._value.get()))
        time_from_phase_start = datetime.timedelta(seconds=int(PHASE_FROM_START._value.get()))

        while timedelta <= current_phase_duration:
            # logger.debug("Light/Dark mode timedelta: %s", timedelta)
            if time_from_phase_start <= timedelta + light_period:
                current_mode = LIGHT_DARK_MODES[0]
                current_mode_duration = light_period
                time_from_mode_start = time_from_phase_start - timedelta
                time_before_mode_end = timedelta + light_period - time_from_phase_start
                break
            if time_from_phase_start >= timedelta + light_period and time_from_phase_start <= timedelta + light_period + dark_period:
                current_mode = LIGHT_DARK_MODES[1]
                current_mode_duration = dark_period
                time_from_mode_start = time_from_phase_start - timedelta - light_period
                time_before_mode_end = timedelta + light_period + dark_period - time_from_phase_start
                break
            timedelta = timedelta + light_period + dark_period

        LIGHT_DARK_MODE.state(current_mode)
        LIGHT_DARK_MODE_DURATION.set(current_mode_duration.seconds)
        LIGHT_DARK_MODE_FROM_START.set(time_from_mode_start.seconds)
        LIGHT_DARK_MODE_BEFORE_FINISH.set(time_before_mode_end.seconds)
        # current_light_dark_mode_metrics()
        logger.info("Current Light/Dark Mode: %s", current_mode)
        logger.debug("Current %s Mode Duration: %s", current_mode, int(LIGHT_DARK_MODE_DURATION._value.get()))
        logger.debug("Time from %s start: %s", current_mode, LIGHT_DARK_MODE_FROM_START._value.get())
        logger.debug("Time before %s finish: %s", current_mode, LIGHT_DARK_MODE_BEFORE_FINISH._value.get())
    except Exception as e:
        logger.debug("Error defining current Light/Dark mode: %s", e)