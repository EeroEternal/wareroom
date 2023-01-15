"""Test cloud object management."""

import pytest

from wareroom import Client, Credential, Bucket


@pytest.mark.parametrize("filename, config_file", [("win.png",
                                                    "tests/data/config.toml")])
def test_delete(filename, config_file):
    """Test delete image file."""

    # read credential from config file
    credential = Credential.from_file(config_file)

    # construct client object, and init bucket object
    client = Client(credential)
    client.bucket = Bucket.from_file(config_file)

    # delete file from cloud storage
    result, content = client.delete(filename)

    assert result is True


@pytest.mark.parametrize("filepath, config_file", [("tests/data/win.png",
                                                    "tests/data/config.toml")])
def test_add(filepath, config_file):
    """Test add image file."""

    # read credential from config file
    credential = Credential.from_file(config_file)

    # construct client object, and init bucket object
    client = Client(credential)
    client.bucket = Bucket.from_file(config_file)

    # get filename from filepath
    filename = filepath.split("/")[-1]

    with open(filepath, "rb") as file:
        # file_content = file.read()
        result, content = client.add(filename, "image/png", file)


        assert result is True


@pytest.mark.parametrize("filename, config_file", [("win.png",
                                                    "tests/data/config.toml")])
def test_get(filename, config_file):
    """Test get image file."""

    # read credential from config file
    credential = Credential.from_file(config_file)

    # construct client object, and init bucket object
    client = Client(credential)
    client.bucket = Bucket.from_file(config_file)

    # get file from cloud storage
    result, content, buffer = client.get(filename)

    print(f'buffer length: {len(buffer)}')

    assert result is True
    assert content == "image/png"
    assert len(buffer) > 0
