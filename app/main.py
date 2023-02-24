from flask import Flask
from api import api
from logger import logger
import time
import config


def create_app():
    logger.info(f'Starting app in {config.APP_ENV} environment')
    app = Flask(__name__)

    app.config.from_object('config')
    api.init_app(app)

    @app.route("/")
    def hello_world():
        time.sleep(50)
        return "<p>Hello, World!</p>"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
