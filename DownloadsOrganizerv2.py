import os
import shutil

path = r"C:/Users/flyin/Downloads/test/"

name = os.listdir(path)

folders = ['Picture Files', 'Music Files', 'Video Files', 'Document Files', 'Miscellaneous']

# Create main category folders
main_categories = ['Pictures', 'Music', 'Video', 'Documents', 'Miscellaneous']
for category in main_categories:
    category_path = os.path.join('C:/Users/flyin', category)
    if not os.path.exists(category_path):
        os.makedirs(category_path)

for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for file in name:
    picture_extensions = [".png", ".jpeg", ".jpg", ".gif", ".svg", ".tiff", ".tif"]
    music_extensions = [".wav", ".mp3", ".aac", ".ogg", ".m4a"]
    video_extensions = [".mp4", ".avi", ".mov", ".flv", ".mkv"]
    document_extensions = [".ppt", ".pptx", ".doc", ".docx", ".csv", ".pdf", ".xls", ".xlsx", ".txt", ".html"]

    if any(ext in file for ext in picture_extensions):
        destination_folder = os.path.join('C:/Users/flyin/Pictures', 'Picture Files')
    elif any(ext in file for ext in music_extensions):
        destination_folder = os.path.join('C:/Users/flyin/Music', 'Music Files')
    elif any(ext in file for ext in video_extensions):
        destination_folder = os.path.join('C:/Users/flyin/Video', 'Video Files')
    elif any(ext in file for ext in document_extensions):
        destination_folder = os.path.join('C:/Users/flyin/Documents', 'Document Files')
    else:
        destination_folder = os.path.join('C:/Users/flyin/Desktop', 'Miscellaneous')

    destination_path = os.path.join(destination_folder, file)

    # Move the file to the destination path
    shutil.move(os.path.join(path, file), destination_path)
