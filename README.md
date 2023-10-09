# Windows_files_sorting

This is a small Python app using the Tkinter library. It will sort files in a Windows directory according to the file type.
## File Sorter
File Sorter is a simple Python application that sorts files in your Downloads folder on Windows. It categorizes files into folders based on their file extensions, making it easier to find and organize your files.

## Requirements
Python 3.7 or later
Tkinter module (pre-installed with Python)
## Usage
To use the File Sorter app, follow these steps:

Clone the repository to your local machine.

Open the terminal or command prompt and navigate to the directory where the file_sorter.py file is saved.

#Run the following command to start the app:

python file_sorter.py
Click the "Sort Files" button to sort the files in your Downloads folder.

After the sorting is complete, a message will be displayed indicating the number of files sorted and the time taken to complete the task.

#Customization
You can customize the file extensions and folder names used by the app by editing the EXTENSIONS and FOLDERS dictionaries in the file_sorter.py file.

#License
This project is licensed under the MIT License.

#Author
This project was created by Ali Akbar Khan. Feel free to contact me at aliakbarkhan161@gmail.com with any questions or feedback.

#Line by line Explanation
Explanation:

The code first imports the necessary modules and creates a Tkinter window with a button to trigger the file sorting function.

The sort_files function gets the path to the Downloads folder using os.path.join(os.path.expanduser("~"), "Downloads"). It then loops through each file in the folder using os.listdir(download_dir).

For each file, it checks if it is a file (not a folder) using os.path.isfile(os.path.join(download_dir, file_name)).

It then gets the file extension using os.path.splitext(file_name)[1] and removes the dot from the extension using file_extension = file_extension[1:].

If the folder for the file extension does not exist, it creates it using os.makedirs(os.path.join(download_dir, file_extension)).

Finally, it renames the file to move it to the appropriate folder using os.rename(os.path.join(download_dir, file_name), os.path.join(download_dir, file_extension, file_name)).

After sorting all the files, it displays a message using messagebox.showinfo("File Sorter", "Files sorted successfully!").

The code then creates a button that triggers the sort_files function when clicked and starts the Tkinter main loop using root.mainloop().
