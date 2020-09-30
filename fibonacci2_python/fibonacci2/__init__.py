from flask import Flask, jsonify, abort, make_response, current_app
from fibonacci2.main.controllers import main
from fibonacci2.admin.controllers import admin
from fibonacci2.config import config
import os
from healthcheck import HealthCheck, EnvironmentDump
from fibonacci2.main.controllers import Calculator
from fibonacci2.cache import cache

app = Flask(__name__)            

config_name = os.getenv("FLASK_CONFIGURATION", "default")
app.config.from_object(config[config_name])
app.config.from_pyfile("config.cfg", silent=True)

cache.init_app(app)
health = HealthCheck(app, "/health")  
envdump = EnvironmentDump(
    app,
    "/environment",
    include_python=True,
    include_os=False,
    include_process=False,
    include_config=True,
)

# add redis function to the healthcheck
def redis_available():
    calc = Calculator()
    calc.fibonacci2(3)
    return True, "redis ok"

health.add_check(redis_available)

def sqlite_available():
    # add precise check against the database
    return True, "sqlite ok"


#health.add_check(sqlite_available)


def application_data():
    return {
        "maintainer": "Billy Chan",
        "git_repo": "https://github.com/billychl1/fibonacci2_python",
    }

envdump.add_section("application", application_data)



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


app.register_blueprint(main, url_prefix="")
app.register_blueprint(admin, url_prefix="/admin")

