import os
import shutil

#print cwd
print("Current working directory: ", os.getcwd())
print('Listing files and directories in the current directory: ', os.listdir('.'))

#create folders and files
folder_name = 'BackupFolder'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f'Folder "{folder_name}" created.')

else:
    print(f'Folder "{folder_name}" already exists.')

#create a sample file
file_name = 'sample.txt'
with open(file_name, 'w') as f:
    f.write('This is a sample file for automation.\n')
    print(f'File "{file_name}" created.')

#move the file to the new folder
shutil.move(file_name, os.path.join(folder_name, file_name))

#rename the file
new_file_name = 'renamed_sample.txt'
os.rename(os.path.join(folder_name, file_name), os.path.join(folder_name, new_file_name))
print(f'File renamed to "{new_file_name}".')

#delete the file
os.remove(os.path.join(folder_name, new_file_name))

#delete the folder
os.rmdir(folder_name)