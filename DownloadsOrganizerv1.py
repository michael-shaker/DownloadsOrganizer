import os
import shutil

path = r"C:/Users/flyin/Downloads/test/"

name = os.listdir(path)

folders = ['Picture Files', 'Music Files', 'Video Files', 'Document Files', 'Miscellaneous']

for folder in folders:
    folder_path = os.path.join(path, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

if not os.path.exists('C:/Users/flyin/Pictures/Picture Files'):
    os.makedirs('C:/Users/flyin/Pictures/Picture Files')
if not os.path.exists('C:/Users/flyin/Documents/Document Files'):
        os.makedirs('C:/Users/flyin/Documents/Document Files')
if not os.path.exists('C:/Users/flyin/Music/Music Files'):
        os.makedirs('C:/Users/flyin/Music/Music Files')
if not os.path.exists('C:/Users/flyin/Video/Video Files'):
        os.makedirs('C:/Users/flyin/Video/Video Files')
if not os.path.exists('C:/Users/flyin/Desktop/Miscellaneous'):
        os.makedirs('C:/Users/flyin/Desktop/Miscellaneous')

for file in name:
    picture_extensions = [".png", ".jpeg", ".jpg", ".gif", ".svg", ".tiff", ".tif"]
    music_extensions = [".wav", ".mp3", ".aac", ".ogg", ".m4a"]
    video_extensions = [".mp4", ".avi", ".mov", ".flv", ".mkv"]
    document_extensions = [".ppt", ".pptx", ".doc", ".docx", ".csv", ".pdf", ".xls", ".xlsx", ".txt", ".html"]

    if any(ext in file for ext in picture_extensions):
        destination_folder = os.path.join(path, "Picture Files")
    elif any(ext in file for ext in music_extensions):
        destination_folder = os.path.join(path, "Music Files")
    elif any(ext in file for ext in video_extensions):
        destination_folder = os.path.join(path, "Video Files")
    elif any(ext in file for ext in document_extensions):
        destination_folder = os.path.join(path, "Document Files")
    else:
        destination_folder = os.path.join(path, "Miscellaneous")

    destination_path = os.path.join(destination_folder, file)

    print(f"Moving {file} to {destination_folder}")

    try:
        shutil.move(os.path.join(path, file), destination_path)
    except Exception as e:
        print(f"Error moving {file}: {e}")

print("File movement completed.")
