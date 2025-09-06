import os

# Define full folder structure
folders = [
    "app/services",
    "app/utils",
    "data/raw",
    "data/processed",
    "tests",
    "docker"
]

# Define files to create
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

# Create all folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create all files if they don’t exist
for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            # Add a placeholder so GitHub shows the file
            if file.endswith(".py"):
                f.write("# " + os.path.basename(file) + " placeholder\n")
            elif file.endswith("README.md"):
                f.write("# Advanced Invoice Parsing and GST Data Extraction System\n")
            elif file.endswith("requirements.txt"):
                f.write("# Add project dependencies here\n")
            elif file.endswith(".gitignore"):
                f.write("venv/\n__pycache__/\n*.pyc\n*.pyo\n*.pyd\n.env\n*.DS_Store\n")
            elif file.endswith("Dockerfile"):
                f.write("# Dockerfile placeholder\n")
            else:
                f.write("")

print("✅ Full project skeleton created/updated successfully!")
