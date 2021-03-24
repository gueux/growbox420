import argparse
from common.logs import MAIN as logger
from models.load import import_db_from_yaml

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Run the Operator')
    parser.add_argument('--db-setup', dest='run_db_setup', action='store_true')

    args = parser.parse_args()

    if args.run_db_setup:
        import_db_from_yaml()
    else:
        logger.info("====================================")
        logger.info(".........Nothing to manage..........")
        logger.info("====================================")