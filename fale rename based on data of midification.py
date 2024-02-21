import os

# Function to rename files in a directory with numbers based on modification time
def rename_files(directory):
    # Get the list of files in the directory
    files = os.listdir(directory)
    
    # Sort files based on modification time
    files.sort(key=lambda x: os.path.getmtime(os.path.join(directory, x)))
    
    # Iterate through the sorted files and rename them with numbers
    for i, file_name in enumerate(files, 1):
        # Construct the new file name with a number prefix
        new_file_name = f"{i}_{file_name}"
        
        # Rename the file
        os.rename(os.path.join(directory, file_name), os.path.join(directory, new_file_name))
        
        # Print the old and new file names for confirmation
        print(f"Renamed: {file_name} -> {new_file_name}")

# Example usage:
directory_path = "."
rename_files(directory_path)
