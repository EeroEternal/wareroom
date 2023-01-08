"""Test add file to OBS."""

import pytest

from wareroom import Client, read_config


@pytest.mark.parametrize("filename, config_file", [("win.png",
                                                    "tests/data/config.toml")])
def test_delete(filename, config_file):
    """Test delete image file."""

    # read access key from config file
    access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

    client = Client(access_key_id, secret_access_key, endpoint)
    result, content = client.delete(bucket, filename)

    assert result is True


@pytest.mark.parametrize("filepath, config_file", [("tests/data/win.png",
                                                    "tests/data/config.toml")])
def test_add(filepath, config_file):
    """Test add image file."""

    # read access key from config file
    access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

    client = Client(access_key_id, secret_access_key, endpoint)

    # get filename from filepath
    filename = filepath.split("/")[-1]

    with open(filepath, "rb") as file:
        # file_content = file.read()
        result, content = client.add(bucket, filename, "image/png", file)


        assert result is True


@pytest.mark.parametrize("filename, config_file", [("win.png",
                                                    "tests/data/config.toml")])
def test_get(filename, config_file):
    """Test get image file."""

    # read access key from config file
    access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

    client = Client(access_key_id, secret_access_key, endpoint)
    result, content, buffer = client.get(bucket, filename)


    assert result is True
