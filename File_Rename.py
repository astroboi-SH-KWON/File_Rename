import os
from os import listdir
from os.path import isfile, join

# OLD_DIR = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_BG"
OLD_DIR = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_D14"
# NEW_DIR = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_BG_UPPER"
NEW_DIR = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_D14_UPPER"

old_files = [f for f in listdir(OLD_DIR) if isfile(join(OLD_DIR,f))]

for old_f_name in old_files:
    old_file = join(OLD_DIR, old_f_name)
    new_file = join(NEW_DIR, old_f_name.upper().replace(".TXT",".txt"))
    os.rename(old_file,new_file)
