# import libraries
from tkinter import *
from tkinter import messagebox, filedialog


def new():
    """
    Delete all text in text box and reset window title to "Untitled - Notepad"

    This function is bound to the "File" > "New" menu option.
    """
    text.delete(1.0, END)
    root.title("Untitled - Notepad")


def open_file():
    """
    Open a file selected from the file dialog and display its contents in the text box.

    This function is bound to the "File" > "Open" menu option.
    """
    file = filedialog.askopenfile(filetypes=[("Text files", "*.txt")])
    if file:
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        root.title(file.name + " - Notepad")
        file.close()


def save():
    """
    Save the current text in the text box to a file.

    This function is bound to the "File" > "Save" menu option.

    If the file already exists, it will be overwritten without warning.
    """
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file:
        file.write(text.get(1.0, END))
        file.close()
        root.title(file.name + " - Notepad")


def save_as():
    """
    Save the current text in the text box to a file chosen by the user.

    This function is bound to the "File" > "Save As" menu option.

    If the file already exists, it will be overwritten without warning.
    """
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file:
        file.write(text.get(1.0, END))
        file.close()
        root.title(file.name + " - Notepad")


def cut():
    """
    Cut the selected text from the text box and add it to the system clipboard.

    This function is bound to the "Edit" > "Cut" menu option.
    """
    text.event_generate("<<Cut>>")


def copy():
    """
    Copy the selected text from the text box to the system clipboard.

    This function is bound to the "Edit" > "Copy" menu option.
    """
    text.event_generate("<<Copy>>")


def paste():
    """
    Paste the contents of the system clipboard into the text box.

    This function is bound to the "Edit" > "Paste" menu option.
    """
    text.event_generate("<<Paste>>")


def about():
    """
    Display a message box with information about the application.

    This function is bound to the "Help" > "About Notepad" menu option.
    """
    messagebox.showinfo("About Notepad", "Notepad v1.0")


def exit():
    """
    Prompt the user to confirm that they want to quit the application.

    If the user selects "OK", the application window is closed using the
    root.quit() method.

    This function is bound to the "File" > "Exit" menu option.
    """
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.quit()


# Create the main application window
root = Tk()
# Set the title of the window to "Notepad"
root.title("Notepad")
# Set the default size of the window to 500x500 pixels
root.geometry("500x500")

# Create a text widget for the main text area
text = Text(root)
# Pack the text widget to expand and fill the window
text.pack(expand=True, fill=BOTH)

# Create a menu bar
menu = Menu(root)
# Configure the root window to display the menu bar
root.config(menu=menu)

# Create a "File" menu
file_menu = Menu(menu)
# Add the "File" menu to the menu bar
menu.add_cascade(label="File", menu=file_menu)
# Add "New" command to the "File" menu
file_menu.add_command(label="New", command=new)
# Add "Open" command to the "File" menu
file_menu.add_command(label="Open", command=open_file)
# Add "Save" command to the "File" menu
file_menu.add_command(label="Save", command=save)
# Add "Save As" command to the "File" menu
file_menu.add_command(label="Save As", command=save_as)
# Add a separator line to the "File" menu
file_menu.add_separator()
# Add "Exit" command to the "File" menu
file_menu.add_command(label="Exit", command=exit)

# Create an "Edit" menu
edit_menu = Menu(menu)
# Add the "Edit" menu to the menu bar
menu.add_cascade(label="Edit", menu=edit_menu)
# Add "Cut" command to the "Edit" menu
edit_menu.add_command(label="Cut", command=cut)
# Add "Copy" command to the "Edit" menu
edit_menu.add_command(label="Copy", command=copy)
# Add "Paste" command to the "Edit" menu
edit_menu.add_command(label="Paste", command=paste)

# Create a "Help" menu
help_menu = Menu(menu)
# Add the "Help" menu to the menu bar
menu.add_cascade(label="Help", menu=help_menu)
# Add "About Notepad" command to the "Help" menu
help_menu.add_command(label="About Notepad", command=about)

# Start the Tkinter event loop
root.mainloop()