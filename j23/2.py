# Create a GUI text editor with basic functionality.

import tkinter as tk
from tkinter import filedialog, messagebox


def new_file():
    """Delete all text in the text area and reset the window title."""
    text_area.delete(1.0, tk.END)


def open_file():
    """Open a text file and display its contents in the text area."""
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        with open(file_path, "r") as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, file.read())


def save_file():
    """Save the contents of the text area to a file."""
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, tk.END))


def cut_text():
    """Cut the selected text from the text area and add it to the system clipboard."""
    text_area.event_generate("<<Cut>>")


def copy_text():
    """Copy the selected text from the text area to the system clipboard.

    This function is bound to the "Edit" > "Copy" menu option.
    """
    text_area.event_generate("<<Copy>>")


def paste_text():
    """
    Paste the contents of the system clipboard into the text area.

    This function is bound to the "Edit" > "Paste" menu option.
    """
    # Generate the paste event for the text area
    text_area.event_generate("<<Paste>>")


# Create the main application window
root = tk.Tk()
# Set the title of the window
root.title("Notepad")

# Create a text area widget with undo functionality enabled
text_area = tk.Text(root, undo=True)
# Pack the text area widget to fill the window and expand with resizing
text_area.pack(fill=tk.BOTH, expand=1)

# Create a menu bar
menu_bar = tk.Menu(root)
# Configure the main window to display the menu bar
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
# Add the "File" menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
# Add "New" command to the "File" menu
file_menu.add_command(label="New", command=new_file)
# Add "Open" command to the "File" menu
file_menu.add_command(label="Open", command=open_file)
# Add "Save" command to the "File" menu
file_menu.add_command(label="Save", command=save_file)
# Add a separator line to the "File" menu
file_menu.add_separator()
# Add "Exit" command to the "File" menu to close the application
file_menu.add_command(label="Exit", command=root.quit)

# Create an "Edit" menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
# Add the "Edit" menu to the menu bar
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# Add "Cut" command to the "Edit" menu
edit_menu.add_command(label="Cut", command=cut_text)
# Add "Copy" command to the "Edit" menu
edit_menu.add_command(label="Copy", command=copy_text)
# Add "Paste" command to the "Edit" menu
edit_menu.add_command(label="Paste", command=paste_text)

# Start the Tkinter event loop
root.mainloop()

