import json
# from pprint import pprint as pp
from classes.exceptions import DataSourceBrokenException


class DataManager:
    def __init__(self, path):
        self.path = path  # путь до файла с нашими данными

    def _load_data(self):
        '''
        Загружает данные из файла для использования другими методами
        :return:
        '''
        try:
            with open(self.path, 'r', encoding = 'utf-8') as file:
                data = json.load(file)
        except:
            raise DataSourceBrokenException('Файл данных поврежден')
        return data

    def _save_data(self, data):
        '''
        Перезаписывает переданные данные в файл с данными
        :param data:
        :return:
        '''
        with open(self.path, 'w', encoding = 'utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)


    def get_all(self):
        '''Отдает полный список данных'''
        data = self._load_data()
        return data

    def search(self, substring):
        '''
        Отдает посты которые содержат substring
        :param substring:
        :return:
        '''
        posts = self._load_data()
        substring = substring.lower()

        mathing_posts = [post for post in posts if substring in post['content'].lower()]
        return mathing_posts

    def add(self, post):
        '''
        Добавляет в хранилище постов определенный пост
        :param post:
        :return:
        '''
        if type(post) != dict:
            raise TypeError('Dict ожидается как тип данных для добавления постов')

        posts = self._load_data()
        posts.append(post)
        self._save_data(posts)

