# Google Takeout Data Unzip and Merge

## Overview

This Python script allows you to efficiently unzip and merge files from a Google Takeout folder into a single destination folder while preserving folder structures. It supports both ZIP archives and individual files within the Takeout folder.

## Prerequisites

- Python 3.x installed on your system.
- Required modules: `shutil`, `zipfile`, `os`, `tqdm`, and `concurrent.futures` (usually included with Python distributions).

## Usage

### 1. Clone or Download the Repository

Clone the repository or download the Python script `Google_Takeout_Data_Unzip_and_Merge.py` from this repository.

### 2. Installation

No installation is required beyond having Python and the required modules installed.

### 3. Running the Script

#### On macOS and Windows:

1. **Open a Terminal or Command Prompt:**
    - macOS: Press `Cmd + Space`, type `Terminal`, and press `Enter`.
    - Windows: Press `Win + R`, type `cmd`, and press `Enter`.

2. **Navigate to the Directory Containing the Script:**

    ```sh
    cd path/to/directory/containing/the/script
    ```

3. **Run the Script:**

    ```sh
    python Google_Takeout_Data_Unzip_and_Merge.py
    ```

4. **Follow the On-Screen Instructions:**
    - When prompted, enter the path to your Google Takeout folder.
    - Enter the path to the output folder where you want to merge the data.

5. **Wait for the Script to Complete:**
    - Progress will be displayed during the extraction and merging process.
    - Once completed, you will see a success message, and the merged data will be available in the output folder.

## Notes

- Ensure that your Google Takeout folder contains the data you wish to extract and merge.
- The script will create the output folder if it does not exist.
- Progress will be displayed during the extraction and merging process.
- In case of any errors, an error message will be shown, and details will be logged in the `unzip_and_merge.log` file.

