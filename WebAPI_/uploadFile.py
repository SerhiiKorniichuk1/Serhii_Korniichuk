from behave import *
from dropbox import *


@given('we have a local file')
def step_check_file(context):
    with open(join(dirname(dirname(dirname(__file__))), 'cat.png'), 'rb'):
        assert True


@when('we send a POST request to https://content.dropboxapi.com/2/files/upload')
def step_upload_file(context):
    context.response = upload_file()


@then('the file is uploaded successfully')
def step_upload_success(context):
    assert context.response.status_code == 200