import os
import json

def write_json(target_path, target_file, data, file_extension=".json"):
    """Write json file to target path."""

    json_object = json.dumps(data, indent=4)
    if not os.path.exists(target_path):
        try:
            os.makedirs(target_path)
        except Exception as e:
            print(e)
            raise
    with open(os.path.join(target_path, target_file+file_extension), 'w') as outfile:
        outfile.write(json_object)
    print(f"File {target_file+file_extension} saved here {target_path}")


def open_json(source_file) -> dict:
    """Open json file and return data."""

    with open(source_file, 'r') as json_read:
        read_buffer = json.load(json_read)
    return read_buffer