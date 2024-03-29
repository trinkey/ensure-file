import os

from typing import Union

def ensure_file(
    path: Union[str, bytes], *,
    folder: bool = False,
    default_value: Union[str, bytes] = b"",
    auto_correct_type: bool = True,
    throw_error: bool = False,
    throw_check_type: bool = True
) -> bool:
    '''Creates a file or folder if it doesn't exist.

    path: string - The file/folder path
    folder: boolean - Whether or not to create a folder instead of a file.
    default_value: string | bytes - The default value to put into a created file (assuming folder is false).
    auto_correct_type: boolean - Whether or not to delete the file and recreate it if it is a folder instead of a file or vice versa.
    throw_error: boolean - Throws an error if the file doesn't exist, instead of creating a new one.
    throw_check_type: boolean - Requires throw_error to be true. This also throws an error if a folder is meant to be a file or vice versa.

    Returns true if a file was created or the file type was swapped and false if the file wasn't created.'''

    # Type checking
    if isinstance(path, bytes):
        path: str = bytes.decode(path)
    if not isinstance(path, str):
        raise TypeError(f"'path' should be str or bytes, not {type(path)}")
    if not isinstance(folder, bool):
        folder: bool = bool(folder)
    if isinstance(default_value, str):
        default_value: bytes = str.encode(default_value)
    if not isinstance(default_value, bytes):
        default_value: bytes = str.encode(str(default_value))
    if not isinstance(auto_correct_type, bool):
        auto_correct_type: bool = bool(auto_correct_type)
    if not isinstance(throw_error, bool):
        throw_error: bool = bool(throw_error)
    if not isinstance(throw_check_type, bool):
        throw_check_type: bool = bool(throw_check_type)

    # Expand the user part of a path
    if path and path[0] == "~":
        path: str = os.path.expanduser(path)

    # Throws the errors if needed
    if throw_error:
        if not os.path.exists(path):
            raise FileNotFoundError(f"The {'folder' if folder else 'file'} at {path} doesn't exist.")

        if throw_check_type and ((os.path.isdir(path) and not folder) or (not os.path.isdir(path) and folder)):
            raise FileExistsError(f"The {'file' if folder else 'folder'} at {path} should be a {'folder' if folder else 'file'}.")

        return False

    if os.path.exists(path):
        # File: exists; Type: Folder; Should be: File
        if auto_correct_type and os.path.isdir(path) and not folder:
            os.rmdir(path)
            f = open(path, "wb")
            f.write(default_value)
            f.close()
            return True

        # File: exists; Type: File; Should be: Fplder
        if auto_correct_type and not os.path.isdir(path) and folder:
            os.remove(path)
            os.mkdir(path)
            return True

        # File: exists; Type: File | Folder; Should be: File | Folder
        return False

    if folder:
        # File: doesn't exist; Should be: Folder
        os.mkdir(path)
    else:
        # File: doesn't exist; Should be: File
        f = open(path, "wb")
        f.write(default_value)
        f.close()

    return True
