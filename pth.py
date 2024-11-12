import os
import winreg

# Get the current directory and specify the folder to add
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_to_add = os.path.join(current_dir, "dist","goku")

def add_to_windows_path(directory):
    with winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        "Environment",
        0,
        winreg.KEY_ALL_ACCESS
    ) as key:
        current_path = winreg.QueryValueEx(key, "PATH")[0]
        if directory not in current_path:
            new_path = current_path + os.pathsep + directory
            winreg.SetValueEx(key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path)
            print("Path added successfully. Restart your terminal or system to apply changes.")
        else:
            print("Directory already exists in PATH.")

add_to_windows_path(folder_to_add)
