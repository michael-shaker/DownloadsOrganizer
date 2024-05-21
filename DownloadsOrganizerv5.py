import os
import shutil

def move_files(source_path, destination_base_path):
    # Define file type extensions mapping to destination folders
    extensions_mapping = {
        'Picture Files': [".png", ".jpeg", ".jpg", ".gif", ".svg", ".tiff", ".tif"],
        'Music Files': [".wav", ".mp3", ".aac", ".ogg", ".m4a"],
        'Video Files': [".mp4", ".avi", ".mov", ".flv", ".mkv"],
        'Document Files': [".ppt", ".pptx", ".doc", ".docx", ".csv", ".pdf", ".xls", ".xlsx", ".txt", ".html"]
    }

    # Define paths for "Documents", "Document Files", "Videos", and "Pictures" folders
    documents_folder = os.path.join(destination_base_path, 'Documents')
    
    # Ensure "Documents" folder exists; create if not present
    os.makedirs(documents_folder, exist_ok=True)

    # Get list of files in the source path
    files = os.listdir(source_path)

    # Iterate through each file and move it to the corresponding destination folder
    for file in files:
        # Initialize the destination folder to "Miscellaneous" by default
        destination_folder = os.path.join(destination_base_path, 'Miscellaneous')

        # Iterate through the defined extensions mapping
        for folder, extensions in extensions_mapping.items():
            # Check if the file extension matches any in the current category
            if any(ext in file for ext in extensions):
                destination_folder = os.path.join(destination_base_path, folder)
                break  # Break out of the inner loop once the file is categorized

        # Create the destination folder if it doesn't exist
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the file to the destination folder
        shutil.move(os.path.join(source_path, file), os.path.join(destination_folder, file))
        print(f"Moved {file} to {destination_folder}")

if __name__ == "__main__":
    # Set the source and destination paths
    source_path = r"C:/Users/flyin/Downloads/test/"
    destination_base_path = r"C:/Users/flyin/" 

    # Call the move_files function with the specified paths
    move_files(source_path, destination_base_path)
