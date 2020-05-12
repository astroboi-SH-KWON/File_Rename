from time import clock

import Util
############### start to set env ###############
############# start lower to upper #############
OLD_DIR_LOWER = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_D14"
NEW_DIR_UPPER = "D:/000_WORK/JiHye/20200325/Base_edit_2/Input/jihye/Query/dABE-LINE/dABE-LINE_D14_UPPER"
############## end lower to upper ##############
############# start rename by rule #############
CHR_PATH = "D:/000_WORK/SongMyunJae_YuGooSang/20200417/WORK_DIR/chlorocebus_sabaeus_chr/"
OLD_NAME_RULE = "Chlorocebus_sabaeus.ChlSab1.1.dna.chromosome."
NEW_NAME_RULE = "chr"

############## end rename by rule ##############

############### end setting env ################


def lower_upper():
    util = Util.Utils()
    util.rename_uppper_lower(OLD_DIR_LOWER, NEW_DIR_UPPER)


def rename_chr_num_fa():
    util = Util.Utils()
    util.rename_by_rules(CHR_PATH, OLD_NAME_RULE, NEW_NAME_RULE)

















start_time = clock()
print("start >>>>>>>>>>>>>>>>>>")
rename_chr_num_fa()
print("::::::::::: %.2f seconds ::::::::::::::" % (clock() - start_time))


