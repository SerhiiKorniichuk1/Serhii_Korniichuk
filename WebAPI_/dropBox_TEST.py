from dropbox import upload_file, get_metadata, delete_file


def test_upload_file():
    assert upload_file().status_code == 100


def test_get_metadata():
    assert get_metadata().status_code == 100


def test_delete_file():
    assert delete_file().status_code == 100