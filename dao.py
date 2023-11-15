import json

from constants import PATH_TO_TEST_DATA
from database import db, Template


def add_user(template):
    try:
        db.session.add(template)
        db.session.commit()
    except:
        db.session.rollback()
        print('Saving user error')


def get_all_templates():
    return Template.query.all()


def get_test_data():
    with open(PATH_TO_TEST_DATA) as file:
        return json.load(file)


def get_test_item_data(test_number):
    data = get_test_data()
    res = None
    for item in data:
        if item['number'] == test_number:
            res = item
    return list(res['data'].items())

# def write_tests_to_json():
#     with open(PATH_TO_TEST_DATA, 'w') as file:
#         file.write(json.dumps([{"number": 1, "data": {"order_date": "10.10.2023", "user_phone":  "+7 999 999 99 99", "user_email":  "vasya@mail.ru", "order_description":  "vasya made an order!"}}, {"number": 2, "data": {"order_date": "12.12.2023", "user_phone":  "+7 999 999 00 00", "user_email":  "vasya@mail.ru", "order_description":  "vasya made an order!"}}]
# , indent=True))


"""create template"""
# main_form_dict = {"order_date": "order_date", "user_phone": "phone", "user_email": "email",
#                   "order_description": "description"}
# main_form = json.dumps(main_form_dict)
# template = Template(form_name='full form', main_form=main_form)
# dao.add_user(template)

"""read template"""
# templates = Template.query.all()
# for template in templates:
#     print(template.main_form)

