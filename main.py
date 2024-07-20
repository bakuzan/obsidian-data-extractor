import json, os

import config
from db import add_or_update_file_data

# Load .env
config.setup()

# Functions
def read_data_file():
    data_path = os.getenv("DATA_FILE_PATH")
    try:
        f = open(data_path)
        data = json.load(f)

        if not data:
            print(f"File({data_path}) empty.")
            exit()
        
        return data["cachedCounts"]
    except:
        print(f"Failed to load file: {data_path}")
        exit()

# Main process
def start():
    print("Starting Obsidian Data Extractor...")
    data = read_data_file()

    for key, value in data.items():
        # Just skip the attachments folder
        if "Attachments" in key:
            continue

        parts = key.split("/")
        file_data = {
            "Location": '/'.join(parts[:-1]),
            "Name": parts[-1],
            "WordCount": value["wordCount"],
            "CreatedDate": value["createdDate"],
            "ModifiedDate": value["modifiedDate"],
        }

        add_or_update_file_data(file_data)

# Run the script contents
if __name__ == "__main__":
    start()