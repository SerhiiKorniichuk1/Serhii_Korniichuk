from behave import *
from dropbox import *


@given('we set the parameters to delete a file from Dropbox')
def step_set_params(context):
    assert True


@when('we send a POST request to https://api.dropboxapi.com/2/files/delete_v2')
def step_delete_file(context):
    context.response = delete_file()


@then('the file is deleted successfully')
def step_delete_success(context):
    assert context.response.status_code == 200