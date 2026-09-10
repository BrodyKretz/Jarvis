import pytest

from jarvis.config import load_settings


def test_defaults(monkeypatch):
    for key in ("JARVIS_DATA_DIR", "JARVIS_LOG_LEVEL", "JARVIS_HOST", "JARVIS_PORT"):
        monkeypatch.delenv(key, raising=False)
    settings = load_settings()
    assert settings.data_dir.name == "data"
    assert settings.log_level == "INFO"
    assert settings.raw_dir.name == "raw"
    assert settings.host == "127.0.0.1"
    assert settings.port == 8000


def test_rejects_bad_log_level(monkeypatch):
    monkeypatch.setenv("JARVIS_LOG_LEVEL", "LOUD")
    with pytest.raises(ValueError, match="JARVIS_LOG_LEVEL"):
        load_settings()


def test_rejects_bad_port(monkeypatch):
    monkeypatch.setenv("JARVIS_PORT", "70000")
    with pytest.raises(ValueError, match="JARVIS_PORT"):
        load_settings()
