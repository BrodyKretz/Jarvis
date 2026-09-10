import logging

from jarvis.config import load_settings


def main() -> None:
    settings = load_settings()
    logging.basicConfig(level=settings.log_level)
    logging.info("jarvis data dir: %s", settings.data_dir)


if __name__ == "__main__":
    main()
