# Windows_files_sorting

This is a small Python app using the Tkinter library. It will sort files in a Windows directory according to the file type.

## File Sorter
File Sorter is a simple Python application that sorts files in your Downloads folder on Windows. It categorizes files into folders based on their file extensions, making it easier to find and organize your files.

## Requirements
- Python 3.7 or later
- Tkinter module (pre-installed with Python)
## Usage
To use the File Sorter app, follow these steps:

Clone the repository to your local machine.

Open the terminal or command prompt and navigate to the directory where the file_sorter.py file is saved.

## Run the following command to start the app:

python file_sorter.py
Click the "Sort Files" button to sort the files in your Downloads folder.

After the sorting is complete, a message will be displayed indicating the number of files sorted and the time taken to complete the task.

## Customization
You can customize the file extensions and folder names used by the app by editing the EXTENSIONS and FOLDERS dictionaries in the file_sorter.py file.

## License
This project is licensed under the MIT License.

## Author
This project was created by Ali Akbar Khan. Feel free to contact me at aliakbarkhan161@gmail.com with any questions or feedback.

# Line by line Explanation
This is a Python script that sorts files in the Downloads folder of the user's computer. It uses the `os` and `tkinter` modules to interact with the file system and create a graphical user interface (GUI) respectively. The script creates a window with a single button labeled "Sort Files". When the button is clicked, the `sort_files()` function is called.

The `sort_files()` function first gets the path to the Downloads folder using the `os.path.join()` and `os.path.expanduser()` methods. It then iterates over all the files in the folder using the `os.listdir()` method. For each file, it checks if it is a file (not a directory) using the `os.path.isfile()` method. If it is a file, it gets the file extension using the `os.path.splitext()` method and extracts the extension string from the resulting tuple. It then checks if a directory with the same name as the extension exists in the Downloads folder using the `os.path.exists()` method. If it does not exist, it creates the directory using the `os.makedirs()` method. Finally, it renames the file to the new directory using the `os.rename()` method.

After all the files have been sorted, a message box is displayed using the `messagebox.showinfo()` method to inform the user that the files have been sorted successfully.
