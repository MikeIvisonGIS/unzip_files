# Import packages/modules
import os, zipfile

# Define folder location
folder = input("Enter a file path: ")
# Ex - folder = r"Anchor\Parent\Name
# Ex - folder = r"C:\file_path\TIGER_Line_Census"

# Walk the entire folder tree and print out the results
for foldername, subfolders, filenames in os.walk(folder):
    print(foldername)
    print(subfolders)
    print(filenames)

# Search for any files that end with .zip.
# For any files that match this criteria, unzip the files into a new folder 
# that matches the same name without the .zip ending.
for filename in filenames:
    if filename.endswith(".zip"):     
        filePath = os.path.join(foldername, filename) # Join variable [folder] with the file ending in [.zip].
        unzipPath = os.path.join(foldername, filename[:-4]) # Define the unzip location
        unzipFolder = zipfile.ZipFile(filePath) # Create a zipfile variable to use
        unzipFolder.extractall(unzipPath) # Unzip the file
        unzipFolder.close() # Close the folder
        os.remove(filePath) # Delete zipped file

