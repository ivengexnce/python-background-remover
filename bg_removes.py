import os
import time
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

SUPPORTED_FORMATS = (".png", ".jpg", ".jpeg", ".webp")

# ---------------------- CORE FUNCTION ----------------------

def remove_bg_file(input_path):
    """Remove background from a single file safely."""
    try:
        if not input_path.lower().endswith(SUPPORTED_FORMATS):
            return False, "Unsupported file format"

        if not os.path.isfile(input_path):
            return False, "File not found"

        folder = os.path.dirname(input_path)
        filename = os.path.basename(input_path)

        name, ext = os.path.splitext(filename)
        output_path = os.path.join(folder, f"{name}_no_bg{ext}")

        # Prevent overwrite
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(folder, f"{name}_no_bg_{counter}{ext}")
            counter += 1

        start = time.time()

        img = Image.open(input_path)
        result = remove(img)
        result.save(output_path)

        end = time.time()

        return True, f"Saved at:\n{output_path}\nTime: {round(end - start, 2)}s"

    except Exception as e:
        return False, str(e)

# ---------------------- UI FUNCTIONS ----------------------

def select_single():
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp")]
    )

    if file_path:
        status_label.config(text="⏳ Processing...")
        root.update()

        success, msg = remove_bg_file(file_path)

        if success:
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)

        status_label.config(text="")

def select_multiple():
    files = filedialog.askopenfilenames(
        title="Select images",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.webp")]
    )

    if files:
        processed = 0

        for file_path in files:
            status_label.config(text=f"Processing: {os.path.basename(file_path)}")
            root.update()

            success, _ = remove_bg_file(file_path)
            if success:
                processed += 1

        status_label.config(text="")
        messagebox.showinfo("Done", f"{processed} images processed successfully!")

# ---------------------- UI SETUP ----------------------

root = tk.Tk()
root.title("Background Remover Tool")
root.geometry("420x300")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="🖼️ Background Remover",
    font=("Segoe UI", 16, "bold")
).pack(pady=10)

# Tagline
tk.Label(
    root,
    text="Fast • Free • No Ads • No Login",
    fg="gray",
    font=("Segoe UI", 9)
).pack()

# Description
tk.Label(
    root,
    text="Select an image or multiple images to remove background",
    wraplength=380,
    font=("Segoe UI", 10)
).pack(pady=10)

# Buttons
tk.Button(
    root,
    text="Select Single Image",
    width=28,
    height=2,
    command=select_single
).pack(pady=5)

tk.Button(
    root,
    text="Select Multiple Images",
    width=28,
    height=2,
    command=select_multiple
).pack(pady=5)

tk.Button(
    root,
    text="Exit",
    width=28,
    height=2,
    command=root.quit
).pack(pady=15)

# Status label
status_label = tk.Label(root, text="", fg="blue", font=("Segoe UI", 9))
status_label.pack()

# Run app
root.mainloop()