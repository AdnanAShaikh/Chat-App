import shutil
import os
import logging

logging.basicConfig(level=logging.INFO)


def copy_files(source_dir, target_dir):
    try:
        # Check if target_dir is a file and rename it if necessary
        if os.path.isfile(target_dir):
            logging.warning(f"Target directory '{
                            target_dir}' is a file. Renaming to avoid overwrite.")
            os.rename(target_dir, f"{target_dir}_backup")

        # Now, proceed with copying files
        if os.path.exists(target_dir):
            logging.info(f"The directory {target_dir} already exists.")
        else:
            os.makedirs(target_dir, exist_ok=True)
            logging.info(f"Created directory {target_dir}.")

        logging.info(f"Attempting to copy files from {
                     source_dir} to {target_dir}.")
        shutil.copytree(source_dir, target_dir)
        logging.info(f"All files successfully copied to {target_dir}.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")


# Specify the source and target directories
source_dir = '.'  # Current directory
target_dir = 'publish'

# Call the function to copy files
copy_files(source_dir, target_dir)
