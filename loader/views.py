from flask import Blueprint, render_template, request, current_app
from classes.data_manager import DataManager
from .exceptions import OutOfFreeNamesError, PictureValueErrorFormat, PictureNotUploadedError
from .upload_manager import UploadManager

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post/', methods=['GET'])
def page_form():
    return render_template('post_form.html')

@loader_blueprint.route('/post/', methods=['POST'])
def page_create_posts():

    path = current_app.config.get('POST_PATH')
    data_manager = DataManager(path)
    upload_manager = UploadManager()

    #Получаем Данные
    picture = request.files.get('picture', None)
    content = request.values.get('content', '')

    #Сохраняем картинку при помощи менеджера загрузок
    filename_saved = upload_manager.save_with_random_filename(picture)

    #Получаем путь для браузера клиента
    web_path = f'/uploads/images/{filename_saved}'

    #создаем данные для записи в файл
    post = {"pic": web_path, "content": content}

    #Добавляем в файл
    data_manager.add(post)

    return render_template('post_uploaded.html', pic=web_path, content=content)

@loader_blueprint.errorhandler(OutOfFreeNamesError)
def error_out_of_free_names(e):
    return 'Закончились имена для загружаемых картинок. Заканчивайте заниматься ерундой - идите погуляйте на улице!'

@loader_blueprint.errorhandler(PictureValueErrorFormat)
def error_picture_value_error_format(e):
    return f'Такой формат картинок не поддерживается данным сайтом <br> <a href="/" class="link">Попробуйте еще раз</a>'

@loader_blueprint.errorhandler(PictureNotUploadedError)
def error_picture_not_upload(e):
    return 'Не удалось произвести загрузку картинки <br> <a href="/" class="link">Попробуйте еще раз</a>'