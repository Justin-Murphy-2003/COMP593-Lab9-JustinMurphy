import requests
import ctypes

def set_image_as_background(img_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, img_path, 0)

def download_image_from_url(img_url, save_path):

    print('Downloading image from URL...')
    response = requests.get(img_url)

    if response.status_code == 200:
        print("success!")
        img_data = response.content
        with open(save_path, 'wb') as file:
                file.write(img_data)
    else:
        print("failed. Response code", response.status_code)
