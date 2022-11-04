from sqlalchemy import create_engine
import pandas as pd

DIALECT = "mysql"
DRIVER = "pymysql"
SCHEMA = "test"


class MockDB:
    def __init__(self, USERNAME, PASSWORD, HOST, PORT):
        self.conn_str = f"{DIALECT}+{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}"
        self.engine = create_engine(self.conn_str)

    def setup(self):
        # create schema
        self.engine.execute(f"DROP SCHEMA IF EXISTS {SCHEMA}")
        self.engine.execute(f"CREATE SCHEMA {SCHEMA} DEFAULT CHARACTER SET 'utf8'")

    def teardown(self):
        # drop schema
        self.engine.execute(f"DROP SCHEMA {SCHEMA}")
