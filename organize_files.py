# import os
# D:\C downloads

import os
import shutil

# Create a new directory for images
os.mkdir("D:\C downloads\Other Files")

# # Get the current directory
# current_dir = os.getcwd()

directory_path = "D:\C downloads"

# Change the current working directory to the specified directory
os.chdir(directory_path)

# Get the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)


# Iterate over all files and directories in the current directory
for root, dirs, files in os.walk(current_dir):
    for file in files:
        # Check if the file is an image file (you can modify the condition based on your file types)
        if file.endswith(".jpg") or file.endswith(".png"):
            # Get the source and destination paths
            src_path = os.path.join(root, file)
            dst_path = os.path.join(current_dir, "Images", file)
            # Move the file to the "Images" directory
            shutil.move(src_path, dst_path)


        elif file.endswith(".pdf") or file.endswith(".docs"):
            # Get the source and destination paths
            src_path = os.path.join(root, file)
            dst_path = os.path.join(current_dir, "Documents", file)
            shutil.move(src_path, dst_path)

        elif file.endswith(".jpeg"):
            # Get the source and destination paths
            src_path = os.path.join(root, file)
            dst_path = os.path.join(current_dir, "WhatsApp Images", file)
            # Move the file to the "Images" directory
            shutil.move(src_path, dst_path)

        else:
            src_path = os.path.join(root, file)
            dst_path = os.path.join(current_dir, "Other Files", file)
            # Move the file to the "Images" directory
            shutil.move(src_path, dst_path)







# # os.makedirs('D:\IMMAGES')
# # current_dir = os.getcwd()


# # Set the path to the directory you want to open and interact with
# directory_path = "D:"

# # Change the current working directory to the specified directory
# os.chdir(directory_path)

# # Get the current working directory
# current_dir = os.getcwd()
# print("Current Directory:", current_dir)

# # List all files and directories in the current directory
# contents = os.listdir(current_dir)
# for item in contents:
#     item_path = os.path.join(current_dir, item)
#     if os.path.isdir(item_path):
#         print("Directory:", item)
#     elif os.path.isfile(item_path):
#         print("File:", item)

