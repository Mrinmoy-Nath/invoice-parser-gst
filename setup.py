import os

# Define folder structure
folders = [
    "app/services",
    "app/utils",
    "data/raw",
    "data/processed",
    "tests",
    "docker"
]

files = [
    "app/__init__.py",
    "app/main.py",
    "app/routes.py",
    "app/services/__init__.py",
    "app/services/ocr.py",
    "app/services/nlp.py",
    "app/services/tables.py",
    "app/services/validation.py",
    "app/utils/__init__.py",
    "app/utils/file_handler.py",
    "app/utils/preprocess.py",
    "tests/__init__.py",
    "tests/test_ocr.py",
    "requirements.txt",
    "README.md",
    ".gitignore",
    "manage.py",
    "docker/Dockerfile"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file in files:
    if not os.path.exists(file):
        open(file, "w").close()

print("✅ Project structure created successfully!")
