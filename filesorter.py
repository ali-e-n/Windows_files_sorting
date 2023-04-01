import os  # Import the os module
import tkinter as tk # Import the tkinter module
from tkinter import messagebox # Import the messagebox module

# Create the root window
root = tk.Tk()
# Set the size of the root window
root.geometry("300x200")
# Set the title of the root window
root.title("File Sorter")

# Define the sort_files function
def sort_files():
    download_dir = os.path.join(os.path.expanduser("~"), "Downloads")
    for file_name in os.listdir(download_dir):
        if os.path.isfile(os.path.join(download_dir, file_name)):
            file_extension = os.path.splitext(file_name)[1]
            file_extension = file_extension[1:]
            if not os.path.exists(os.path.join(download_dir, file_extension)):
                os.makedirs(os.path.join(download_dir, file_extension))
            os.rename(os.path.join(download_dir, file_name), os.path.join(download_dir, file_extension, file_name))
    messagebox.showinfo("File Sorter", "Files sorted successfully!")

# Create the sort button
sort_button = tk.Button(root, text="Sort Files", command=sort_files)
sort_button.pack(pady=20)

root.mainloop()
