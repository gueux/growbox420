import os
from common.utils import read_yaml
from common.config import DATA_PATH
from common.logs import MAIN as logger
from common.storage import RDB, connector as rdb_connector
from rethinkdb.errors import RqlRuntimeError, RqlDriverError

def import_db_from_yaml():
    data_tree = []
    for index, tree in enumerate(os.walk(DATA_PATH)):
        if index > 0:
            data_tree.append(tree) 

    for data in data_tree:
        
        database = data[0].split('/')[-1]

        connection = rdb_connector()
        try:
            RDB.db_create(database).run(connection)
            logger.info("Database `%s` setup completed", database)
        except RqlRuntimeError:
            logger.error("Database `%s` already exists", database)
        except RqlDriverError as e:
            logger.error(e)
            exit()
        finally:
            connection.close()

        tables = data[2]

        for table in tables:
            table_name = os.path.splitext(table)[0]
            table_data = read_yaml(DATA_PATH + '/' + database + '/' + table)
            connection = rdb_connector()
            try:
                RDB.db(database).table_create(table_name).run(connection)
                RDB.db(database).table(table_name).insert(table_data).run(connection)
                logger.info("Table `%s` setup in database `%s` completed", table_name, database)
            except RqlRuntimeError:
                logger.error("Table `%s` in database `%s` already exists", table_name, database)
            except RqlDriverError as e:
                logger.error(e)
                exit()
            finally:
                connection.close()