import json
from datetime import datetime

import dao
from constants_for_checks import PHONE_CHECK_LIST, ALLOWED_DOMAINS


def check_keys(data):
    """Проверяет, все ли ключи формы есть среди ключей переданных данных"""
    templates = dao.get_all_templates()
    for template in templates:
        template_keys = json.loads(template.main_form).keys()
        if set(template_keys).issubset(set(data.keys())):
            return template
    return False


def check_date(data):
    """Валидация даты"""
    try:
        format_date = "%d.%m.%Y" if data.count('.') == 2 else "%Y-%m-%d"
        datetime.strptime(data, format_date)
        return True
    except ValueError:
        return False


def check_phone(data):
    """Валидация номера телефона"""
    if len(data) == 16 and data.startswith('+7 '):
        data = data.lstrip('+7 ').split()
        if all([item.isdigit() for item in data]):
            return [len(item) for item in data] == PHONE_CHECK_LIST


def check_mail(data):
    """Валидация электронной почты"""
    if data.count('@') == 1:
        data = data.split('@')
        if data[1].count('.') == 1:
            data = data[1].split('.')
            return data[1] in ALLOWED_DOMAINS


def check_description(data):
    """Валидация текста. По заданию не нужно её делать, но там же указано, что она должна быть последней.
    Я подумал о возможности такой проверки в дальнейшем, и, пока что она стоит последней, как в задании"""
    print('check_description: ', data)
    return True
