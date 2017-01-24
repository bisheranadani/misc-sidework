import os

def rename_files():
    file_list = os.listdir(r"C:\Python27\udacity\prank")
    print(file_list)
    saved_path = os.getcwd()
    print("Current working directory is " + saved_path)

    os.chdir(r"C:\Python27\udacity\prank")

    for file_name in file_list:
        print("Old name - " + file_name)
        print("New Name - " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "123456789"))

    os.chdir(saved_path)
    
rename_files()
