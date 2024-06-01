# File Management



This Python script automatically organizes files and folders within your Downloads directory based on their file extensions. It neatly categorizes them into appropriate folders, such as "Images," "Videos," "Documents," etc. It also handles duplicate file names by appending a number to the end of the file name.

## Technologies Used

* **Python:** The core programming language used for this script.
* **os Module:** Provides a way to interact with the operating system, enabling actions like file manipulation and directory creation.
* **shutil Module:** Offers high-level file operations like moving and copying.

## How It Works

1. **Target Directory:** The script starts by targeting your "Downloads" folder.
2. **Extension Mapping:** It uses a dictionary (`extensions`) to map file extensions (e.g., `.jpg`, `.mp4`, `.docx`) to corresponding folder names.
3. **Scanning Files:** It iterates through every file and subfolder in your Downloads directory.
4. **Categorization:**
    * **Files:**
        * The script extracts the file extension.
        * It uses the `extensions` dictionary to determine the target folder.
        * If the folder doesn't exist, it's created.
        * The file is moved to the appropriate folder. If a file with the same name exists, the script appends a number to the end of the new file's name.
    * **Folders:**
        * Folders are moved to a dedicated "Folders" subdirectory within the Downloads directory. If a folder with the same name exists, the script appends a number to the end of the new folder's name.
5. **Duplicate Handling:** The script checks for existing files or folders in the target location. If a duplicate exists, it adds a number in parentheses to the filename or folder name (e.g., "document (1).pdf").



## License

This project is licensed under the MIT License - see the LICENSE file for details.
