import os
import random

from loader.exceptions import OutOfFreeNamesError, PictureValueErrorFormat, PictureNotUploadedError


class UploadManager:
    def get_free_filename(self, folder, file_type):

        attempts = 0
        RANGE_OF_IMAGE_NUBMBERS = 100
        LIMITS_OF_ATEMPTS = 1000

        while True:
            pic_name = str(random.randint(0, RANGE_OF_IMAGE_NUBMBERS))
            filename_to_save = f'{pic_name}.{file_type}'
            os_path = os.path.join(folder, filename_to_save)
            is_filename_occupied = os.path.exists(os_path)

            if not is_filename_occupied:
                return filename_to_save

            attempts += 1

            if attempts > LIMITS_OF_ATEMPTS:
                raise OutOfFreeNamesError('No more free names to save Image')

    def is_file_type_valied(self, file_type):
        if file_type.lower() in ['jpeg', 'gif', 'png', 'jpg', 'webp', 'tiff']:
            return True
        return False

    def save_with_random_filename(self, picture):

        # Работаем с картинкой

        filename = picture.filename
        file_type = filename.split('.')[-1]

        # Проверяем валидность формата картинки
        if not self.is_file_type_valied(file_type):
            raise PictureValueErrorFormat(f'Формат {file_type} не поддерживается')

        # Получаем свободное имя
        folder = os.path.join('.', 'uploads', 'images')
        filename_to_save = self.get_free_filename(folder, file_type)

        # Сохраняем под новым именем
        try:
            picture.save(os.path.join(folder, filename_to_save))
        except:
            raise PictureNotUploadedError(f'{folder, filename_to_save}')

        return filename_to_save
