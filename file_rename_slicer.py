import os

def change_file_names(directory_path):
    # Get a list of all files in the directory
    files = os.listdir(directory_path)

    # Iterate through each file
    for file_name in files:
        if ".py" in file_name:
            continue

        # Construct the new file name using slicing
        # lengthhh = len("_7e0f33e77d6b81677a7d725ed0ae9911_15")
        lengthhh = 1
        new_file_name = file_name[lengthhh:] 

        # Create the full paths for the old and new file names
        old_path = os.path.join(directory_path, file_name)
        new_path = os.path.join(directory_path, new_file_name)

        # Rename the file
        os.rename(old_path, new_path)

        print(f"Renamed: {file_name} to {new_file_name}")

# Specify the directory path where you want to change file names
directory_path = "."

# Call the function to change file names in the specified directory
change_file_names(directory_path)
