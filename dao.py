import json

from constants import PATH_TO_TEST_DATA
from database import Template


def get_all_templates():
    """Возвращает объекты всех шаблонов"""
    return Template.query.all()


def get_test_data():
    """Возвращает тестовые данные"""
    with open(PATH_TO_TEST_DATA) as file:
        return json.load(file)


def get_test_item_data(test_number):
    """Возвращает данные теста по его номеру для отображения на странице информации о тесте"""
    data = get_test_data()
    res = None
    print(data)
    for item in data:
        if item['number'] == test_number:
            res = item
    return list(res.items())
