from behave import *
from dropbox import *


@given('we set the parameters to get metadata from Dropbox')
def step_set_params(context):
    assert True


@when('we send a POST request to https://api.dropboxapi.com/2/files/get_metadata')
def step_get_metadata(context):
    context.response = get_metadata()


@then('the metadata is returned successfully')
def step_metadata_success(context):
    assert context.response.status_code == 200