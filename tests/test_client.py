"""Test add file to OBS."""

import pytest

from wareroom import Client

import tomllib


def read_config(filepath, kind='storage'):
    """Read storage config from toml file.

    Args:
        filepath (str): toml config file path.
        kind (str): config kind, only storage now.
    Returns:
        (str, str, str, str): access_id, secret_key, endpoint, bucket.
    """
    with open(filepath, "rb") as f:
        config = tomllib.load(f)

        access_key_id = config["storage"]["access_key_id"]
        secret_access_key = config["storage"]["secret_access_key"]
        endpoint = config["storage"]["endpoint"]
        bucket = config["storage"]["bucket"]
        return access_key_id, secret_access_key, endpoint, bucket


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
