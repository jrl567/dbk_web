from PIL import Image
import os

# Source and destination folders
src_dir = "images"
dst_dir = os.path.join(src_dir, "thumbs")

# Create thumbnails directory if missing
os.makedirs(dst_dir, exist_ok=True)

# Loop through all files in source
for filename in os.listdir(src_dir):
    if filename.lower().endswith(".jpg"):
        src_path = os.path.join(src_dir, filename)
        dst_path = os.path.join(dst_dir, filename)

        try:
            # Open the image
            with Image.open(src_path) as img:
                # Create thumbnail (keeps aspect ratio)
                img.thumbnail((400, 400))
                # Save to destination
                img.save(dst_path, "JPEG", quality=70)
                print(f"Created thumbnail: {dst_path}")
        except Exception as e:
            print(f"❌ Failed on {filename}: {e}")
