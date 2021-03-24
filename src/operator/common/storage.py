from sys import exit
from rethinkdb import RethinkDB
from rethinkdb.errors import RqlRuntimeError, RqlDriverError
from common.config import RDB_HOST, RDB_PORT, PLANT
from common.logs import MAIN as logger

RDB = RethinkDB()

def connector():
    try:
        connection = RDB.connect(host=RDB_HOST, port=RDB_PORT)
    except RqlDriverError:
        logger.error("No database connection could be established by address: %s:%s", RDB_HOST, RDB_PORT)
        exit()
    return connection