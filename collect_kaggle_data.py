import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("shivamb/netflix-shows")

print("Path to dataset files:", path)

shutil.copy(
    os.path.join(path, "netflix_titles.csv"),
    "netflix_titles.csv"
)