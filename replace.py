import os
import glob
import shutil

def replace_roblox_cursor():
    local_app_data = os.environ.get('LOCALAPPDATA')
    if not local_app_data:
        print("ERROR: Could not find LOCALAPPDATA environment variable.")
        return

    roblox_versions_path = os.path.join(local_app_data, "Roblox", "Versions")
    
    if not os.path.exists(roblox_versions_path):
        print(f"ERROR: Roblox versions directory not found at: {roblox_versions_path}")
        print("Please ensure Roblox is installed on this user account.")
        return

    version_folders = glob.glob(os.path.join(roblox_versions_path, "version-*"))
    if not version_folders:
        print("ERROR: No Roblox version folders found.")
        return
    
    latest_version_folder = max(version_folders, key=os.path.getmtime)
    print(f"SUCCESS: Found latest Roblox version: {os.path.basename(latest_version_folder)}")

    cursor_dir = os.path.join(latest_version_folder, "content", "textures", "Cursors", "KeyboardMouse")
    
    if not os.path.exists(cursor_dir):
        print(f"ERROR: Cursor directory not found inside the version folder: {cursor_dir}")
        return

    user_cursors = ["pointer.png", "hover.png", "text.png"]
    target_cursors = ["ArrowFarCursor.png", "ArrowCursor.png", "IBeamCursor.png"]

    print("TASK: Replacing cursors...")
    index = 0
    for cursor in target_cursors:
        target_path = os.path.join(cursor_dir, cursor)
        backup_path = target_path + ".bak"

        if os.path.exists(target_path) and not os.path.exists(backup_path):
            shutil.copy2(target_path, backup_path)
            print(f"SUCCESS: Created backup: {cursor}.bak")
        try:
            shutil.copy2(user_cursors[index], target_path)
            print(f"SUCCESS: Replaced: {cursor}")
        except Exception as e:
            print(f"ERROR: Failed to replace {cursor}: {e}")
        
        index += 1
    print("SUCCESS: Restart Roblox to see your new cursor.")

replace_roblox_cursor()
input("Press any key to continue... ")
