"""
   Algorithms Wep API application / main file / entry point,
   with configure routing map and application server start up
"""
from app.app import app
from app.config import Config


def run():
    app.logger.info('PyFlaskAlgorithmsAPI - web API startup')
    app.run(port=Config.PORT_API_APP, debug=Config.DEBUG_GLOBAL, host=Config.HOST_API_APP)


# run it as server (for development server mod)
if __name__ == '__main__':
    run()
