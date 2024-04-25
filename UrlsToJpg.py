import os
import requests

# Create a folder if it doesn't exist
folder_path = r'F:\Tinder Storage\Undefined'
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

# Open the URLs file and read the lines
with open('urls.txt', 'r') as file:
    lines = file.readlines()

# Initialize a counter for naming the images
counter = 1

# Loop through the lines and extract image URLs
for line in lines:
    if line.startswith('https://'):
        # Get the URL
        url = line.strip()

        # Send a GET request to the URL
        response = requests.get(url)
        
        # Check if request was successful
        if response.status_code == 200:
            # Determine file name
            file_name = f'image_{counter}.jpg'
            file_path = os.path.join(folder_path, file_name)
            
            # Save the image to the folder
            with open(file_path, 'wb') as img_file:
                img_file.write(response.content)
                
            print(f'Saved {file_name}')
            counter += 1
        else:
            print(f'Failed to fetch {url}')
