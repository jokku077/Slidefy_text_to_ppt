import requests
import os
from PIL import Image
from io import BytesIO
from duckduckgo_search import DDGS

def download_image(url, save_path):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        image_data = BytesIO(response.content)
        image = Image.open(image_data)

        # Create directories if they don't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        image.save(save_path)
        print("Image downloaded and verified successfully!")
    except Exception as e:
        print(f"Error downloading or verifying image: {e}")

def get_image(topic, count):
    results = DDGS().images(topic, region='wt-wt', safesearch='off', max_results=20)
    i = 0
    paths = []
    for image in results:
        try:
            url = image['image']
            folder = topic.replace(' ','-')
            folder_path = f'images\\{folder}'
            extension = url.split('.')[-1].split('?')[0]
            file_path = f'{folder_path}\\image{i}.{extension}'
            i += 1
            download_image(url, file_path)
            paths.append(file_path)
            print(paths)
        except Exception as e:
            print(f"Error downloading image: {e}")
        if i == count:
            break
    
    return paths
