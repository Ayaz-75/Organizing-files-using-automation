import os
import shutil

# os.makedirs('D:\Downloads\Images')
# os.makedirs('D:\Downloads\DOCS')


directory_path = 'D:\Downloads'

os.chdir(directory_path)

current_dir = os.getcwd()

print(f'Current directory: {current_dir}')

for root, dir, files in os.walk(current_dir):
    for file in files:
        src_path = os.path.join(root, file)
        try:
            if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.jpg'):
                dst_path = os.path.join(root, 'Images', file)
                shutil.move(src_path, dst_path)
            elif file.endswith('.pdf'):
                dst_path = os.path.join(root, 'PDFs', file)
                shutil.move(src_path, dst_path)
            elif file.endswith(".docx"):
                dst_path = os.path.join(root, 'DOCS', file)
                shutil.move(src_path, dst_path)
            
        except:
            FileExistsError("File already exists")

        