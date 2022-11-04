import logging

from src.repository.db_repository import DBRepository


# TODO: Add detailed docstrings
class MyService:
    def __init__(self, config: dict, db_repository: DBRepository) -> None:
        #        logger.debug(f"MHPMService.__init__(): initializing with config {config}")

        self.config = config
        self.db_repository = db_repository

    #        logger.debug(f"MHPMService.__init__(): initialized")

    def do_something(self) -> dict:
        """
        Do something
        """
        self.db_repository.sample_query()
        return dict(ok=True)
