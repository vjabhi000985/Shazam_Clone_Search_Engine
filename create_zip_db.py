import shutil
import os

def zip_db_folder(db_folder_path, output_zip_path):
  """Creates a zip archive of a given folder."""
  try:
      # Create a temporary base name for the archive (without extension)
      base_name = os.path.splitext(output_zip_path)[0]  # Remove .zip if it exists

      # Create the zip archive
      shutil.make_archive(base_name, 'zip', db_folder_path)

      # Move the archive to the desired output path (if needed)
      if base_name + ".zip" != output_zip_path : # if the paths are different.
        shutil.move(base_name + ".zip", output_zip_path)

      print(f"Successfully created zip archive: {output_zip_path}")

  except FileNotFoundError:
      print(f"Error: Folder not found at {db_folder_path}")
  except Exception as e:
      print(f"An error occurred: {e}")

# Calling the function to compressing the db file.
db_folder_path = "./db"
output_zip_path = "db.zip" 
zip_db_folder(db_folder_path, output_zip_path) 