import os
from rembg import remove
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def remove_bg_file(input_path):
    """Remove background from a single file."""
    if not os.path.isfile(input_path):
        messagebox.showerror("Error", f"File not found:\n{input_path}")
        return
    
    folder = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    output_path = os.path.join(folder, "no_bg_" + filename)
    
    try:
        img = Image.open(input_path)
        result = remove(img)
        result.save(output_path)
        messagebox.showinfo("Success", f"Background removed!\nSaved at:\n{output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def select_file():
    """Open file dialog to select one image."""
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if file_path:
        remove_bg_file(file_path)

def select_multiple_files():
    """Open file dialog to select multiple images."""
    files = filedialog.askopenfilenames(
        title="Select images",
        filetypes=[("Image files", "*.png *.jpg *.jpeg")]
    )
    if files:
        for file_path in files:
            remove_bg_file(file_path)


root = tk.Tk()
root.title("Windows Background Remover")
root.geometry("400x250")


tk.Label(root, text="🖼️ Background Remover", font=("Segoe UI", 16, "bold")).pack(pady=10)
tk.Label(root, text="Select an image or multiple images to remove background", wraplength=380).pack(pady=5)


tk.Button(root, text="Select Single Image", width=25, command=select_file).pack(pady=10)
tk.Button(root, text="Select Multiple Images", width=25, command=select_multiple_files).pack(pady=10)
tk.Button(root, text="Exit", width=25, command=root.quit).pack(pady=20)

root.mainloop()