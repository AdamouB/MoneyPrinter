import os
import pytest
from Backend import utils


def test_check_env_vars_all_set(monkeypatch):
    monkeypatch.setenv('PEXELS_API_KEY', 'key')
    monkeypatch.setenv('TIKTOK_SESSION_ID', 'sid')
    monkeypatch.setenv('IMAGEMAGICK_BINARY', '/path/magick')

    # Should not raise SystemExit
    utils.check_env_vars()


def test_check_env_vars_missing(monkeypatch):
    monkeypatch.delenv('PEXELS_API_KEY', raising=False)
    monkeypatch.setenv('TIKTOK_SESSION_ID', 'sid')
    monkeypatch.setenv('IMAGEMAGICK_BINARY', '/path/magick')

    with pytest.raises(SystemExit):
        utils.check_env_vars()
