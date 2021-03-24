from common.config import PLANT
from common.logs import MAIN as logger
from common.storage import RDB, connector as rdb_connector
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

DB_NAME = 'lifecycles'

def get_lifecycle(item):
    lifecycle = []
    connection = rdb_connector()
    logger.info("Loading lifecycle for `%s` from storage", item)
    cursor = RDB.db(DB_NAME).table(item).order_by('order').run(connection)
    for phase in cursor:
        lifecycle.append(phase)
    logger.debug("Loaded lifecycle: %s", lifecycle)
    return lifecycle

LIFECYCLE = get_lifecycle(PLANT)