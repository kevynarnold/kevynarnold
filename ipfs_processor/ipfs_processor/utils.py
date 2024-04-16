import os
import yaml

def ensure_directory(path):
    os.makedirs(path, exist_ok=True)

def load_config():
    with open('ipfs_processor/config.yaml', 'r') as file:
        return yaml.safe_load(file)
