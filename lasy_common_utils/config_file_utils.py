import os
from pathlib import Path
from lasy_ops.connection import LasyConnections

def custom_config_exists():
    base_path = Path(LasyConnections().config_file_full_path())
    # custom_config_file_path = "lasy_config_data.json"
    # full_path = base_path.joinpath(custom_config_file_path)
    return os.path.exists(base_path)