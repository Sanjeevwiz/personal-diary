import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os
from datetime import datetime

# Function to save the diary entry
def save_entry():
    entry_date = entry_date_field.get()
    entry_text = text_diary_entry.get("1.0", "end-1c")  # Get the content of the text box

    # If the entry is empty, show an error message
    if not entry_text.strip():
        messagebox.showerror("Error", "Diary entry cannot be empty!")
        return

    # Check if date is provided, if not, set it to today's date
    if not entry_date:
        entry_date = datetime.now().strftime("%Y-%m-%d")

    # Create a file path using the date
    file_name = f"diary_entries/{entry_date}.txt"

    # Ensure the directory exists
    if not os.path.exists("diary_entries"):
        os.makedirs("diary_entries")

    # Save the entry to the file
    with open(file_name, 'w') as file:
        file.write(entry_text)

    messagebox.showinfo("Success", "Diary entry saved successfully!")
    clear_entry_fields()  # Clear the fields after saving

# Function to clear the entry fields
def clear_entry_fields():
    entry_date_field.delete(0, tk.END)
    text_diary_entry.delete("1.0", "end")

# Function to view a saved diary entry
def view_entry():
    # Ask user for the date to view
    entry_date = simpledialog.askstring("View Entry", "Enter the date (YYYY-MM-DD):")

    if entry_date:
        # Check if the file for that date exists
        file_name = f"diary_entries/{entry_date}.txt"
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                diary_content = file.read()
            # Display the content in the text box
            text_diary_entry.delete("1.0", "end")
            text_diary_entry.insert("1.0", diary_content)
        else:
            messagebox.showerror("Error", f"No diary entry found for {entry_date}")

# Function to delete a saved entry
def delete_entry():
    entry_date = simpledialog.askstring("Delete Entry", "Enter the date (YYYY-MM-DD) to delete:")

    if entry_date:
        # Check if the file for that date exists
        file_name = f"diary_entries/{entry_date}.txt"
        if os.path.exists(file_name):
            os.remove(file_name)
            messagebox.showinfo("Success", f"Diary entry for {entry_date} deleted successfully.")
            clear_entry_fields()  # Clear the entry fields after deletion
        else:
            messagebox.showerror("Error", f"No diary entry found for {entry_date}")

# GUI Setup
root = tk.Tk()
root.title("Personal Diary Application")

# Title Label
title_label = tk.Label(root, text="Personal Diary", font=("Helvetica", 24))
title_label.pack(pady=10)

# Date Entry Field
date_label = tk.Label(root, text="Date (YYYY-MM-DD):", font=("Helvetica", 12))
date_label.pack(pady=5)

entry_date_field = tk.Entry(root, font=("Helvetica", 12), width=20)
entry_date_field.pack(pady=5)

# Diary Entry Field (Multi-line Text Box)
entry_label = tk.Label(root, text="Write your diary entry:", font=("Helvetica", 12))
entry_label.pack(pady=5)

text_diary_entry = tk.Text(root, font=("Helvetica", 12), width=50, height=10)
text_diary_entry.pack(pady=10)

# Buttons for Save, View, Delete, and Clear
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

save_button = tk.Button(frame_buttons, text="Save Entry", font=("Helvetica", 12), command=save_entry)
save_button.grid(row=0, column=0, padx=10)

view_button = tk.Button(frame_buttons, text="View Entry", font=("Helvetica", 12), command=view_entry)
view_button.grid(row=0, column=1, padx=10)

delete_button = tk.Button(frame_buttons, text="Delete Entry", font=("Helvetica", 12), command=delete_entry)
delete_button.grid(row=0, column=2, padx=10)

clear_button = tk.Button(frame_buttons, text="Clear Fields", font=("Helvetica", 12), command=clear_entry_fields)
clear_button.grid(row=0, column=3, padx=10)

# Start the GUI
root.mainloop()