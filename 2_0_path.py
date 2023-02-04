# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

import os

path = os.getcwd()
print(path)

file = path + '\sample.txt'
print(file)

dir = os.chdir(path + '/algorithm')
dir_path = os.getcwd()
print(dir_path)

abs_path = os.path.abspath('../')
print(abs_path)

abs_file_path = os.path.abspath(__file__)
print(abs_file_path)

base_dir = os.path.dirname(abs_file_path)
print(base_dir)

base_file = os.path.basename(abs_file_path)
print(base_file)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
