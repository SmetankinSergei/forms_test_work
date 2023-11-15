from flask import render_template, request

import dao
import utils
from main import app


@app.route('/', )
def start_page():
    return render_template('start_page.html')


@app.route('/show_templates')
def show_templates():
    templates_view = utils.get_templates_views()
    return render_template('show_templates.html', templates=templates_view)


@app.route('/run_tests')
def run_tests():
    tests = dao.get_test_data()
    return render_template('run_tests.html', tests=tests)


@app.route('/show_test_data/<int:test_number>')
def show_test_data(test_number):
    test_data = dao.get_test_item_data(test_number)
    return render_template('show_test_data.html', test_data=test_data)


@app.route('/get_form/', methods=['POST'])
def get_form():
    data = request.form.to_dict()
    resp = utils.create_response(data)
    return render_template('get_form.html', resp=resp)
