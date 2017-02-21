#-*- coding=utf-8 -*-

import sys
import os, os.path
import shutil
import json

RESULT_FILE = 'AllImageList.json'
RESULT_FILE_OVER_TWO = 'AllImageListOverTwo.json'
CONFIG_FILE = 'DirectionList.json'
RESOURCE_FOLDER = 'AllResource'

all_image_list_over_two = {}
all_image_list = {}
copy_res_folder = ''

def ReadConfig(path_root):
    path = os.path.normpath(os.path.join(path_root, CONFIG_FILE))
    try:
        f = open(path)
        cfg = json.load(f, encoding='utf8')
        f.close()
    except:
        print("Configuration file \"%s\" is not existed or broken!" % path)
    finally:
        f.close()
    return cfg

def list_image_file(file_path, file_name):
#   圖片複製到資料夾
    image_full_path = os.path.join(file_path, file_name)
    if not all_image_list.get(file_name):
        all_image_list[file_name] = [image_full_path]
        shutil.copy(image_full_path, copy_res_folder)
    else:
        all_image_list[file_name].append(image_full_path)
        all_image_list_over_two[file_name] = all_image_list[file_name]
    
def list_image_file_in_folder(folder_path):
#    print(folder_path);
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if item.endswith('.png') or item.endswith('.jpg'):
            list_image_file(folder_path, item)
        elif os.path.isdir(item_path):
            list_image_file_in_folder(item_path)

def check_files(root_path):
    folder_list = config_resource_folder_list['file_list']
    for folder_name in folder_list:
        folder_path = os.path.join(root_path, folder_name)
        print(folder_path);
        if os.path.isdir(folder_path):
            list_image_file_in_folder(folder_path)
            
def CreateJsonFile(data, filename):
    try:
        jsondata = json.dumps(data, indent=4, skipkeys=True, sort_keys=True)
        fd = open(filename, 'w')
        fd.write(jsondata)
        fd.close()
    except:
        print 'ERROR writing', filename
        pass

# -------------- main --------------
if __name__ == '__main__':
    print( "== Check image files ==" )
    
    current_dir = os.path.dirname(os.path.realpath(__file__))
#   建立所有圖檔資料夾
    copy_res_folder = os.path.join(current_dir, RESOURCE_FOLDER)
    if os.path.exists(copy_res_folder):
        shutil.rmtree(copy_res_folder)
    else:
        os.mkdir(copy_res_folder)
        

    config_resource_folder_list = ReadConfig(current_dir)
#    luac_exe_path = os.path.join(current_dir, "luac.exe")
    all_in_one_root = os.path.join(current_dir, "../..")
    check_files(all_in_one_root);
    
    result_file_path = os.path.join(current_dir, RESULT_FILE)
    CreateJsonFile(all_image_list, result_file_path)
    
    result_file_path_over_two = os.path.join(current_dir, RESULT_FILE_OVER_TWO)
    CreateJsonFile(all_image_list_over_two, result_file_path_over_two)
    
    print( "== Done ==" )