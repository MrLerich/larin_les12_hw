import logging
from flask import Flask, send_from_directory

from main.views import main_blueprint
from loader.views import loader_blueprint
import loggers

app = Flask(__name__)
#Регистрируем blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

app.config['POST_PATH'] = 'data/posts.json'
app.config['UPLOAD_FOLDER'] = 'uploads/images'

loggers.create_logger()

logger = logging.getLogger("basic")

#Добавляет возможность просмотра загруженных картинок, помимо папки static
@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

logger.info("Приложение стартует")

app.run(debug=True)




