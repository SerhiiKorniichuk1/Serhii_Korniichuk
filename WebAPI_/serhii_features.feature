Feature: Dropbox API

    Scenario: Upload File
        Given we have a local file
        When we send a POST request to https://content.dropboxapi.com/2/files/upload
        Then the file is uploaded successfully

    Scenario: Get Metadata
        Given we set the parameters to get metadata from Dropbox
        When we send a POST request to https://api.dropboxapi.com/2/files/get_metadata
        Then the metadata is returned successfully

    Scenario: Delete File
        Given we set the parameters to delete a file from Dropbox
        When we send a POST request to https://api.dropboxapi.com/2/files/delete
        Then the file is deleted successfully