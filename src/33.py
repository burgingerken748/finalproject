import os

def append_to_file(file_path, content):
    """
    Appends content to a file.
    
    Parameters:
        file_path (str): The path to the file where the content will be appended.
        content (str): The string content that you want to append.

    Returns:
        None
    """
    with open(file_path, 'a') as file:
        file.write(content)
