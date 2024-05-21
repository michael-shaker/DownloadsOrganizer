import os
import shutil

def organize_files(source_path, destination_base_path):
    extensions_mapping = {
        'Picture Files': [".png", ".jpeg", ".jpg", ".gif", ".svg", ".tiff", ".tif"],
        'Music Files': [".wav", ".mp3", ".aac", ".ogg", ".m4a"],
        'Video Files': [".mp4", ".avi", ".mov", ".flv", ".mkv"],
        'Document Files': [".ppt", ".pptx", ".doc", ".docx", ".csv", ".pdf", ".xls", ".xlsx", ".txt", ".html"]
    }

    for folder, extensions in extensions_mapping.items():
        destination_folder = os.path.join(destination_base_path, folder)
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

    files = os.listdir(source_path)

    for file in files:
        for folder, extensions in extensions_mapping.items():
            if any(ext in file for ext in extensions):
                destination_folder = os.path.join(destination_base_path, folder)
                destination_path = os.path.join(destination_folder, file)
                shutil.move(os.path.join(source_path, file), destination_path)
                print(f"Moved {file} to {destination_folder}")
                break

if __name__ == "__main__":
    source_path = r"C:/Users/flyin/Downloads/test/"
    destination_base_path = r"C:/Users/flyin/"

    organize_files(source_path, destination_base_path)