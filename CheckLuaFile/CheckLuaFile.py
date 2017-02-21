import sys
import os, os.path
import shutil

def check_lua_file(file_path):
    commandStr = luac_exe_path + " " + file_path;
    exe_return = os.system(commandStr)
    if 0 != exe_return:
        print("== Error!! == ")
        print("FilePath: " + file_path)
        os.system("pause")

def check_lua_file_in_folder(folder_path):
#    print(folder_path);
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if item.endswith('.lua'):
            check_lua_file(item_path)
        elif os.path.isdir(item_path):
            check_lua_file_in_folder(item_path)

def check_files(root_path):
    folder_list = ["GtMobile/Lua", "GtMobile/LuaCommon"]
    for folder_name in folder_list:
        folder_path = os.path.join(root_path, folder_name)
        if os.path.isdir(folder_path):
            check_lua_file_in_folder(folder_path)

# -------------- main --------------
if __name__ == '__main__':
    print( "== Check lua files ==" )
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
    luac_exe_path = os.path.join(current_dir, "luac.exe")
    all_in_one_root = os.path.join(current_dir, "../..")
    check_files(all_in_one_root);
    
    print( "== Good! No error ==" )
    os.system("pause")