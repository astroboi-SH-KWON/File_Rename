import os
from os import listdir
from os.path import isfile, join


class Utils:
    def __init__(self):
        self.txt_ext = ".txt"

    """
    rename_uppper_lower :
    :param
        old_dir
        new_dir
        flag : True (lower -> upper) , False (upper -> lower)
    """
    def rename_uppper_lower(self, old_dir, new_dir, flag=True):
        old_files = [f for f in listdir(old_dir) if isfile(join(old_dir, f))]

        for old_f_name in old_files:
            old_file = join(old_dir, old_f_name)
            if flag:
                new_file = join(new_dir, old_f_name.upper().replace(".TXT", self.txt_ext))
                os.rename(old_file, new_file)
            else:
                new_file = join(new_dir, old_f_name.lower())
                os.rename(old_file, new_file)

    def rename_by_rules(self, dir_path, old_name_rule, new_name_rule):
        old_files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]

        for old_f_name in old_files:
            old_file = join(dir_path, old_f_name)
            # rename rules
            new_f_name = old_f_name.replace(old_name_rule, new_name_rule)

            new_file = join(dir_path, new_f_name)
            os.rename(old_file, new_file)