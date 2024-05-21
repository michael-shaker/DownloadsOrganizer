import os
import shutil

def move_files(source_path, destination_base_path):
    pdf_destination_folder = os.path.join(destination_base_path, 'Documents', 'Document Files')
    mp4_destination_folder = os.path.join(destination_base_path, 'Videos', 'Video Files')

    for folder in [pdf_destination_folder, mp4_destination_folder]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    files = os.listdir(source_path)

    for file in files:
        if file.lower().endswith(".pdf"):
            destination_path = os.path.join(pdf_destination_folder, file)
            shutil.move(os.path.join(source_path, file), destination_path)
            print(f"Moved {file} to {pdf_destination_folder}")

        elif file.lower().endswith(".mp4"):
            destination_path = os.path.join(mp4_destination_folder, file)
            shutil.move(os.path.join(source_path, file), destination_path)
            print(f"Moved {file} to {mp4_destination_folder}")

if __name__ == "__main__":
    source_path = r"C:/Users/flyin/Downloads/test/"
    destination_base_path = r"C:/Users/flyin/"

    move_files(source_path, destination_base_path)