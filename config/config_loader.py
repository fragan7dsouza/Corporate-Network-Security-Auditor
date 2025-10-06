import json
import os
from utils.logger import log_error

CONFIG_FILE = os.path.join("config", "settings.json")

def load_config():
    """Loads configuration from the settings.json file."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        log_error(f"Configuration file not found at: {CONFIG_FILE}. Using default values.")
        return None
    except json.JSONDecodeError as e:
        log_error(f"Error decoding JSON in {CONFIG_FILE}: {e}")
        return None
SETTINGS = load_config()