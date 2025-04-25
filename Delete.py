import os
import time

directories = [
    "E:/porbandhar/code/cropped_images"
]

age_threshold = 45 * 86400  # 45 days in sec

current_time = time.time()

image_extensions = ['.img', '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

def delete_old_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                file_path = os.path.join(root, filename)

                file_age = current_time - os.path.getmtime(file_path)

                if file_age > age_threshold:
                    try:
                        os.remove(file_path)
                        print(f"Deleted: {file_path}")
                    except Exception as e:
                        print(f"Error deleting {file_path}: {e}")

while True:
    for top_level_directory in directories:
        if os.path.exists(top_level_directory):
            print(f"Checking files in: {top_level_directory}")
            delete_old_files(top_level_directory)
        else:
            print(f"Directory does not exist: {top_level_directory}")
            
    time.sleep(600)
