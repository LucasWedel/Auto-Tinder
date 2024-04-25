import os

# Define the directory where the images are stored
image_dir = r'C:\Users\lucas\OneDrive\Documents\UNI Software\Tinders\billeder'

# Get a list of all files in the directory
files = os.listdir(image_dir)

# For each file in the directory
for filename in files:
    # If the file is a .jpg and its name starts with '0_' or '1_'
    if filename.endswith('.jpg') and (filename.startswith('0_') or filename.startswith('1_')):
        # Create the new name by removing the first 2 characters
        new_name = filename[2:]
        # Rename the file
        os.rename(os.path.join(image_dir, filename), os.path.join(image_dir, new_name))
