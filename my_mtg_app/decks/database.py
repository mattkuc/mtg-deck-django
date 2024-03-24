
import os
from urllib import request

def download_card(card_name,card_set,foil):

    if foil:
        pass
    else:
        pass

    api_url = f"https://api.scryfall.com/cards/named?{encoded_card_name}"
    pass

def download_set_cards(card_data):
    pass


def save_card_to_db(card_data):
    pass

def save_image_to_folder(image_url,folder_path, filename):
    response = request.get(image_url)
    
    if response.status_code == 200:
        image_data = response.content
        file_path = os.path.join(folder_path, filename)

        with open(file_path, 'wb') as image_file:
            image_file.write(image_data)

        print(f"Image saved successfully: {file_path}")
        return file_path
    else:
        print(f"Error: Unable to fetch image from {image_url}")
        return None



