import os
import shutil
import datetime

def create_copy(directory, days_to_keep=10):
    current_date = datetime.datetime.now()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            creation_date = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
            age_in_days = (current_date - creation_date).days
            if age_in_days > days_to_keep:

                version = 1
                while True:
                    new_filename = f"{filename}_v{version:04d}"
                    new_file_path = os.path.join(directory, new_filename)
                    if not os.path.exists(new_file_path):
                        break
                    version += 1

                shutil.copy2(file_path, new_file_path)
                print(f"File '{filename}' copied as '{new_filename}'")


if __name__ =="__main__":
    # Example usage:
    directory_to_check = 'your_directory_path_here'
    days_to_keep = 10
    create_copy(directory_to_check, days_to_keep)
