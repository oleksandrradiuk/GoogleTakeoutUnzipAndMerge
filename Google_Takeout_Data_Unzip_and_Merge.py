import os
import shutil
import zipfile
from tqdm import tqdm
import logging
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(filename='unzip_and_merge.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def unzip_and_merge(takeout_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Count the total number of files to process
    total_files = sum(len(files) for _, _, files in os.walk(takeout_folder))
    progress = tqdm(total=total_files, desc='Progress', unit='file')

    # Function to extract or copy files
    def process_file(file_path):
        if file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                for member in zip_ref.infolist():
                    # Construct the complete file path
                    file_full_path = os.path.join(output_folder, member.filename)
                    # If the file already exists, rename it with a suffix
                    while os.path.exists(file_full_path):
                        base, ext = os.path.splitext(file_full_path)
                        file_full_path = f"{base}_1{ext}"
                    # Extract the file with its folder structure preserved
                    zip_ref.extract(member, output_folder)
        else:
            # Maintain the folder structure while copying the file
            relative_path = os.path.relpath(file_path, takeout_folder)
            output_file_path = os.path.join(output_folder, relative_path)
            # If the file already exists, rename it with a suffix
            while os.path.exists(output_file_path):
                base, ext = os.path.splitext(output_file_path)
                output_file_path = f"{base}_1{ext}"
            os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
            shutil.copy(file_path, output_file_path)
        progress.update(1)

    # Process files concurrently for better performance
    with ThreadPoolExecutor() as executor:
        for root, _, files in os.walk(takeout_folder):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(process_file, file_path)

    # Close the progress bar
    progress.close()

if __name__ == "__main__":
    try:
        takeout_folder = input("Enter the path to your Google Takeout folder: ")
        output_folder = input("Enter the path to the output folder where you want to merge the data: ")

        # Validate input paths
        if not os.path.exists(takeout_folder) or not os.path.exists(output_folder):
            raise FileNotFoundError("Input or output folder does not exist.")
        
        unzip_and_merge(takeout_folder, output_folder)
        print("Data extraction and merging completed successfully.")

        # Log success
        logging.info("Data extraction and merging completed successfully.")
    
    except Exception as e:
        # Log errors
        logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
