import os

for folderName, subfolders, filenames in os.walk('./'):
    print(f'The folder is {folderName}')
    print(f'The subfolders in {folderName} are {subfolders}')
    print(f'The filenames in {folderName} are {filenames}')
    print()
