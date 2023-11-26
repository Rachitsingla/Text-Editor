import tkinter as tk
from tkinter import filedialog, scrolledtext, Menu, ttk
from transformers import pipeline


# Loading the summarization pipeline
summarizer = pipeline("summarization")

def create_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "w") as file:
            pass  # Creating an empty file
        status_bar.config(text=f"File '{filename}' created successfully.")

def open_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "r") as file:
            file_content = file.read()
            text_area.delete(1.0, tk.END)  # Clear the text area
            text_area.insert(tk.END, file_content)
        status_bar.config(text=f"Opened file '{filename}'.")

def save_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "w") as file:
            file.write(text_area.get(1.0, tk.END))
        status_bar.config(text=f"File saved as '{filename}'.")

def append_to_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "a") as file:
            appended_text = text_area.get(1.0, tk.END)
            file.write(appended_text)
        status_bar.config(text="Text appended successfully.")

def delete_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        import os
        os.remove(filename)
        status_bar.config(text=f"File '{filename}' deleted successfully.")

def summarize_text():
    text = text_area.get(1.0, tk.END)
    summarized_text = summarizer(text, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    text_area.delete(1.0, tk.END)  # Clear the text area
    text_area.insert(tk.END, summarized_text)
    status_bar.config(text="Text summarized.")

def increase_font_size():
    current_size = text_area.cget("font").split()[1]
    new_size = int(current_size) + 2
    text_area.configure(font=("Arial", new_size))
    status_bar.config(text=f"Font size increased to {new_size}.")

def decrease_font_size():
    current_size = text_area.cget("font").split()[1]
    new_size = int(current_size) - 2 if int(current_size) >= 4 else int(current_size)
    text_area.configure(font=("Arial", new_size))
    status_bar.config(text=f"Font size decreased to {new_size}.")

# Create the main window
root = tk.Tk()
root.title("Shree Ram Text Editor")
root.geometry("800x600")
icon_path = '613bKgWBHcL.ico'
root.iconbitmap(icon_path)

# Create a text area
text_area = scrolledtext.ScrolledText(root, wrap="word", font=("Arial", 12))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

# Create a menu
menu_bar = Menu(root)
root.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=create_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save As", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Append", command=append_to_file)
edit_menu.add_command(label="Summarize", command=summarize_text)
edit_menu.add_separator()
edit_menu.add_command(label="Increase Font Size", command=increase_font_size)
edit_menu.add_command(label="Decrease Font Size", command=decrease_font_size)

# Create a status bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Start the main loop
root.mainloop()
