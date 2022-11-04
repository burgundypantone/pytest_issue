import os

from dependency_injector import containers, providers

from src.repository.db_repository import DBRepository
from src.service.MyService import MyService

config_file_path = {
    "INT": "./src/conf/int_config.yaml",
    "LOCAL": "./src/conf/local_config.yaml",
    "PREPROD": "./src/conf/preprod_config.yaml",
    "PROD": "./src/conf/prod_config.yaml",
    "TEST": "./conf/test_config.yaml",
}

print("!!!!!!!!! in containers.py !!!!!!!!!!")


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routes"])
    print(f"$$$$$$$\npingu  - {os.environ.get('ENV')}\n$$$$$$")
    config = providers.Configuration(
        yaml_files=[
            "./src/conf/common.yaml",  # load the common config first
            config_file_path[
                os.environ.get("ENV", "LOCAL")
            ],  # env specific config - will override values in common.yaml
        ]
    )
    config.load(envs_required=True)
    print(f"$$$$$$$\nconfig  loaded as - {config.get('app')}\n$$$$$$")
    db_repository = providers.Resource(DBRepository, config.get("app.db_repository"))

    my_service = providers.Factory(
        MyService, config.get("app.my_service"), db_repository
    )
