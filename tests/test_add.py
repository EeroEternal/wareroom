"""Test add file to OBS."""

import pytest

from wareroom import Client, read_config


@pytest.mark.parametrize("filepath, config_file", [("../data/win.png",
                                                    "../data/config.toml")])
def test_add(filepath, config_file):
    """Test add image file."""

    # read access key from config file
    access_key_id, secret_access_key, endpoint, bucket = read_config(config_file)

    client = Client(access_key_id, secret_access_key, endpoint)
    result, content = client.add(bucket, "win.png", "image/png", filepath)

    assert result.status < 300
    print(f'add image result content: {content}')