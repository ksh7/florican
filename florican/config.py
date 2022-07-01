import logging
import os
import yaml


__all__ = ["BASE_DIR", "CONFIG_FILE", "BROKER_DIR", "CONFIG", "DB_FILENAME"]

BASE_DIR = os.getenv("FLORICAN_BASE_DIR", os.path.expanduser("~/.florican"))
CONFIG_FILE = os.getenv("FLORICAN_CONFIG", os.path.join(BASE_DIR, "config.yaml"))
SCHEDULER_DIR = os.getenv("FLORICAN_SCHEDULER_DIR", os.path.join(BASE_DIR, "scheduler"))
BROKER_DIR = os.getenv("FLORICAN_BROKER_DIR", os.path.join(BASE_DIR, "broker"))
DB_FILENAME = os.getenv("FLORICAN_DB_FILENAME", os.path.join(BASE_DIR, "db.json"))
LOG_FILE = os.getenv("FLORICAN_LOG_FILE", os.path.join(BASE_DIR, "florican.log"))
PID_FILE = os.getenv("FLORICAN_PID_FILE", os.path.join(BASE_DIR, "florican.pid"))


def load_config() -> dict:
    """Parse the config from a given file."""
    try:
        with open(CONFIG_FILE, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError as e:
        raise FileNotFoundError("Could not find config file, please run `florican init`.")
    except yaml.YAMLError as e:
        logging.error(f"Could not parse config: {e}")
        exit(1)
