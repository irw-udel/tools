import os

path = r"path\to\folder"
extensions = set(os.path.splitext(name)[-1] for root, dirs, files in os.walk(path) for name in files)

with open("file_extensions.txt", "w") as f:
    for extension in extensions:
        f.write(f"*{extension}, ")