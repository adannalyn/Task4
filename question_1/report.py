import json

def save_goods(file_path, dict_list):
    try:
        with open(file_path, 'w') as f:
            json.dump(dict_list, f, indent=2)
    except IOError:
        print("Failed to save file")

def load_goods(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
