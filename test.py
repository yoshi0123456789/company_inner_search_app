from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_DB_DIR = os.getenv("CHROMA_DB_DIR")
