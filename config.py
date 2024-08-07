from dotenv import load_dotenv
import os


def setup():
    load_dotenv(override=True)
    print("USING ENV", os.getenv("ENV"))
    print("USING DATABASE_PATH", os.getenv("DATABASE_PATH"))
    print("USING DATA_FILE_PATH", os.getenv("DATA_FILE_PATH"))