import json

import dao


def check_keys(data):
    templates = dao.get_all_templates()
    for template in templates:
        template_keys = json.loads(template.main_form).keys()
        if set(template_keys).issubset(set(data.keys())):
            return template.form_name
    return False


def check_date(data):
    pass


def check_phone(data):
    pass


def check_mail(data):
    pass


def check_description(data):
    pass
