import pytest

from jarvis.config import load_settings


def test_defaults(monkeypatch):
    monkeypatch.delenv("JARVIS_DATA_DIR", raising=False)
    monkeypatch.delenv("JARVIS_LOG_LEVEL", raising=False)
    settings = load_settings()
    assert settings.data_dir.name == "data"
    assert settings.log_level == "INFO"
    assert settings.raw_dir.name == "raw"


def test_rejects_bad_log_level(monkeypatch):
    monkeypatch.setenv("JARVIS_LOG_LEVEL", "LOUD")
    with pytest.raises(ValueError, match="JARVIS_LOG_LEVEL"):
        load_settings()
