import os
from rembg import remove
from PIL import Image
import tkinter as tk
from tkinter import filedialog


root = tk.Tk()
root.withdraw()

print("🖼️ Welcome to the Interactive Background Remover!")

while True:
    mode = input("\nDo you want to type the path manually or browse for a file?\n" "(Type 'type' or 'T', 'browse' or 'B', 'exit' or 'E' to quit): ").strip().lower()

    if mode == "exit" or mode == "e":
        print("👋 Exiting. Goodbye!")
        break
    elif mode == "type" or mode == "t":
        input_path = input("Enter the full path of the image: ").strip()
    elif mode == "browse" or mode == "b":
        print("Select an image file...")
        input_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.png *.jpg *.jpeg")]
        )
        if not input_path:
            print("👋 No file selected. Exiting.")
            break
    else:
        print("Please type 'type'/'t', 'browse'/'b', or 'exit'/'e'.")
        continue


    
    if not os.path.isfile(input_path):
        print("❌ File not found. Check the path and try again.")
        continue
    folder = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    output_path = os.path.join(folder, "no_bg_" + filename)

    print("⏳ Removing background...")
    try:
        input_image = Image.open(input_path)
        output_image = remove(input_image)
        output_image.save(output_path)
        print(f"✅ Background removed successfully! Saved at: {output_path}")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")

    while True:
        choice = input("\nDo you want to remove background from another image? (y/n): ").strip().lower()
        if choice in ["y", "yes"]:
            break  
        elif choice in ["n", "no"]:
            print("Thank you, Have a Good Day! Sir  ")
            exit()
        else:
            print("Please type 'y' or 'n'.")