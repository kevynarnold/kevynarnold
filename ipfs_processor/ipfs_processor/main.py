import os
import json
from PIL import Image
import piexif
from datetime import datetime, timedelta
import random
from .utils import ensure_directory, load_config

def random_date(start, end):
    """Generate a random datetime between `start` and `end`."""
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def process_images(input_dir, output_png_dir, config):
    ensure_directory(output_png_dir)
    image_files = [f for f in os.listdir(input_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif'))]
    data_list = []
    edition = int(config['edition'])  # Start edition from the config file

    # Define the date range for random dates
    start_date = datetime.strptime("2020-01-01", "%Y-%m-%d")
    end_date = datetime.strptime("2024-01-01", "%Y-%m-%d")

    for file_name in image_files:
        img_path = os.path.join(input_dir, file_name)
        img = Image.open(img_path)

        exif_dict = {
            "0th": {
                piexif.ImageIFD.Artist: config['compiler'],
                piexif.ImageIFD.ImageDescription: config['description'],
            },
            "Exif": {
                piexif.ExifIFD.DateTimeOriginal: random_date(start_date, end_date).strftime("%Y:%m:%d %H:%M:%S"),
            }
        }
        exif_bytes = piexif.dump(exif_dict)
        
        output_filename = os.path.splitext(file_name)[0] + '.png'
        output_path = os.path.join(output_png_dir, output_filename)
        img.save(output_path, "PNG", exif=exif_bytes)
        
        data = {
            'image': f"ipfs://{config['cid']}/{output_filename}",
            'description': config['description'],
            'edition': edition,
            'date': random_date(start_date, end_date).strftime("%Y-%m-%d %H:%M:%S"),
            'compiler': config['compiler']
        }
        data_list.append(data)
        edition += 1  # Increment edition for each image
    
    return data_list

def save_data_as_json(data_list, output_json_dir):
    ensure_directory(output_json_dir)
    for data in data_list:
        json_filename = os.path.splitext(data['image'].split('/')[-1])[0] + '.json'
        file_path = os.path.join(output_json_dir, json_filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

def main():
    config = load_config()
    data_list = process_images(config['input_dir'], config['output_png_dir'], config)
    save_data_as_json(data_list, config['output_json_dir'])

if __name__ == '__main__':
    main()
