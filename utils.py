import json

import dao
from checks import check_keys, check_date, check_phone, check_mail, check_description


def get_templates_views():
    templates = dao.get_all_templates()
    views = []
    for template in templates:
        template_body = template.main_form.strip('{}').split(', ')
        view = {'template_name': template.form_name,
                'template_body': template_body}
        views.append(view)
    return views


def create_response(data):
    data = prepare_data_to_check(data)
    template_name = check_keys(data)
    check_list = []
    if template_name:
        check_list.append(check_date(data))
        check_list.append(check_phone(data))
        check_list.append(check_mail(data))
        check_list.append(check_description(data))
        if all(check_list):
            return template_name
    else:
        create_bad_response(data)


def prepare_data_to_check(data):
    data = str(data['text'])
    while "'" in data:
        data = data.replace("'", '"')
    data = json.loads(data)['data']
    data = data.split('&')
    data = {x.split('=')[0]: x.split('=')[1] for x in data}
    return data


def create_bad_response(data):
    pass
