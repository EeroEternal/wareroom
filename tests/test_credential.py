"""Test cloud storage credential."""

import pytest

from wareroom import Credential


@pytest.mark.parametrize("config_file", ["tests/data/config.toml"])
def test_fromfile(config_file):
    """Test credential from file."""

    credential = Credential.from_file(config_file)

    print(f'credential: {credential}')
    assert credential.access_key is not None
    assert credential.secret_key is not None

