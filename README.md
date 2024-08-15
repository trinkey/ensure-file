> [!NOTE]  
> This repository has been **migrated** to [git.gay](https://git.gay/trinkey/ensure-file). The Github version will **no longer be maintained**.

# Ensure File
An easy way to manage file creation

Example usage:
```py
from ensure_file import ensure_file as ef

# This will create a file in the user directory under the `.example` folder
# if the file doesn't already exist. If the file does exist, nothing happens.
# Along with that, it will return true if a file is created, and false if
# nothing happens. This applies to everything else going forward.
ef("~/.example/foo.txt")

# Using the `default_value` parameter, you can set the default value to be
# written to the file. If the file already exists, nothing happens.
import json
ef("./bar.json", default_value=json.dumps({
  "foo": "bar"
}))

# If you want to create a folder, you can set the `folder` parameter to true.
ef("/tmp/foo", folder=True)

# If there is already a folder with the same name as a file you want to create,
# the folder will be deleted and overwritten. This can be disabled by setting
# the `auto_correct_type` to false. In this function call, nothing would happen
# because of the folder created on the previous line.
ef("/tmp/foo", folder=False, auto_correct_type=False)

# If you want to not actually create any files or folders and instead throw an
# error if a file or folder doesn't exist, you can easily do so by setting the
# `throw_error` parameter to true. By default, this will also throw an error
# if the file or folder is the wrong type, such as checking if the file you're
# checking has the same name as a folder in the same directory. The type
# checking can be disabled by setting the `throw_check_type` parameter to
# false.
try:
    ef("./some/file.css", folder=False, throw_error=True)
    print("The file exists!")

except FileNotFoundError:
    print("The file doesn't exist!")
except FileExistsError:
    print("A folder exists where there should be a file!")
```
