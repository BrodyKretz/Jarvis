import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
VALID_LOG_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}


@dataclass(frozen=True)
class Settings:
    data_dir: Path
    log_level: str

    @property
    def raw_dir(self) -> Path:
        return self.data_dir / "raw"

    @property
    def processed_dir(self) -> Path:
        return self.data_dir / "processed"


def load_settings() -> Settings:
    data_dir = Path(os.getenv("JARVIS_DATA_DIR", "data"))
    if not data_dir.is_absolute():
        data_dir = PROJECT_ROOT / data_dir

    log_level = os.getenv("JARVIS_LOG_LEVEL", "INFO").upper()
    if log_level not in VALID_LOG_LEVELS:
        raise ValueError(
            f"JARVIS_LOG_LEVEL must be one of {sorted(VALID_LOG_LEVELS)}, got {log_level!r}"
        )

    return Settings(data_dir=data_dir, log_level=log_level)
