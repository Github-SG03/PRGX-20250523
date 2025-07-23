# ==== IMPORTS ====
import os
# === CONFIGURATION ===
folder_path = r"C:\Users\Shivam Gupta\OneDrive\Documents\Shivam_Developement\PYTHON\python_other\30_days_beginner_programming_challenge"  # <- change this
keep_files = {'practice.py'}  # <- filenames to keep

# === DELETE SCRIPT ===
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if filename.endswith('.py') and filename not in keep_files:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")
