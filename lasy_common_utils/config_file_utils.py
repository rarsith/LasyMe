import os
from pathlib import Path
from lasy_ops.connection import ConfigPath

def custom_config_exists():
    base_path = Path(ConfigPath)
    custom_config_file_path = "lasy_config_data.json"
    full_path = base_path.joinpath(custom_config_file_path)
    return os.path.exists(full_path)