import os.path

from checks import check_phone, check_date, check_mail, check_description

PATH_TO_TEST_DATA = os.path.join('test_data', 'test.json')

TYPES_CHECKS = {
    'main_date': check_date,
    'phone': check_phone,
    'email': check_mail,
    'description': check_description
}

TEMPLATE_TYPES = ['main_date', 'phone', 'email', 'description']
