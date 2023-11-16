import json

import dao
from checks import check_keys
from constants import TYPES_CHECKS, TEMPLATE_TYPES


def get_templates_views():
    templates = dao.get_all_templates()
    views = []
    for template in templates:
        view = {'template_name': template.form_name}
        view.update(json.loads(template.main_form))
        views.append(view)
    return views


def create_response(data):
    data = prepare_data_to_check(data)
    template = check_keys(data)
    if template and check_types(template, data):
        return template.form_name
    else:
        return create_bad_response(data)


def check_types(template, data):
    check_list = []
    template = json.loads(template.main_form)
    for template_key, template_type in template.items():
        check_list.append(TYPES_CHECKS[template_type](data[template_key]))
    if check_list:
        return all(check_list)


def prepare_data_to_check(data):
    data = str(data['text'])
    while "'" in data:
        data = data.replace("'", '"')
    data = json.loads(data)['data']
    data = data.split('&')
    data = {x.split('=')[0]: x.split('=')[1] for x in data}
    return data


def create_bad_response(data):
    bad_response = {}
    for data_key in data.keys():
        for template_type in TEMPLATE_TYPES:
            if TYPES_CHECKS[template_type](data[data_key]):
                bad_response[data_key] = template_type
                break
    return bad_response
