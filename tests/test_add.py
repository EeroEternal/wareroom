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
    print(f'delete image result content: {content}')



@pytest.mark.parametrize("filepath, config_file", [("tests/data/win.png",
                                                    "tests/data/config.toml")])
def test_add(filepath, config_file):
    """Test add image file."""

    # read access key from config file
    access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

    client = Client(access_key_id, secret_access_key, endpoint)
    result, content = client.add(bucket, "win.png", "image/png", filepath)

    print(f'result: {result}')

    assert result is True
    print(f'add image result content: {content}')



