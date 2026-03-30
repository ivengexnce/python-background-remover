import os
from rembg import remove
from PIL import Image


input_path = input("Enter the path of the image: ").strip()

if not input_path:
    print("❌ No input path provided. Exiting.")
    exit()

if not os.path.isfile(input_path):
    print("❌ File not found. Check the path.")
    exit()

folder = os.path.dirname(input_path)
filename = os.path.basename(input_path)
output_path = os.path.join(folder, "no_bg_" + filename)

print("⏳ Removing background...")


input_image = Image.open(input_path)
output_image = remove(input_image)

output_image.save(output_path)

print("✅ Background removed successfully!")
print(f"📁 Saved at: {output_path}")