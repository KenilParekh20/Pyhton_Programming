import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_FOLDER = BASE_DIR / 'uploads'
DATABASE = BASE_DIR / 'instance' / 'app.db'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024 

# create required folders if missing
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(BASE_DIR / 'instance', exist_ok=True)