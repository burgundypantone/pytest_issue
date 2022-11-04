import logging
import os
import unittest

from src import create_app

app = create_app()
app.app_context().push()


def run():
    """Run the application"""
    logging.info("Import config for env={0}".format(os.environ.get("ENV", "INT")))
    app.run()


def test():
    """Run unit tests"""
    tests = unittest.TestLoader().discover(pattern="test*.py", start_dir="./test")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    run()
