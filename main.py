import config
from db import add_or_update_file_data

# Load .env
config.setup()

# Functions
def read_data_file():
    print("TODO")
    data = None

    if not data:
        print(f"Could not find file")
        exit()

# Main process
def start():
    print("Starting Obsidian Data Extractor...")
    items = read_data_file()

    for item in items:
        file_data = {}
        # Extract the data

        add_or_update_file_data(file_data)

# Run the script contents
if __name__ == "__main__":
    start()