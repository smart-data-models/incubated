import os
import shutil

root_dir = "/home/aabella/PycharmProjects/incubated/ZEB"
source_dir = "/home/aabella/PycharmProjects/data-models/templates/dataModel_for_submision"  # Current directory (where script runs)

for subdir in os.listdir(root_dir):
    subdir_path = os.path.join(root_dir, subdir)
    if os.path.isdir(subdir_path):
        # Copy all files (excluding subdirectories to avoid recursion)
        for item in os.listdir(source_dir):
            src_path = os.path.join(source_dir, item)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, subdir_path)
            elif os.path.isdir(src_path) and item != subdir:  # Avoid copying into itself
                dest_path = os.path.join(subdir_path, item)
                shutil.copytree(src_path, dest_path, dirs_exist_ok=True)
        print(f"Copied tree to: {subdir_path}")