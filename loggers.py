import logging

def create_logger():

    logger = logging.getLogger('basic')
    logger.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('logs/basic.log')

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    #Добавляем форматтеры
    log_format = logging.Formatter('%(asctime)s :  %(message)s')

    console_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)