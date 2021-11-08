import os
import re
path='F:\会计专硕3班\QQ邮箱 - 副本'
def str_insert(str_origin,pos,str_add):
    str_list=list(str_origin)
    str_list.insert(pos,str_add)
    str_out=''.join(str_list)
    return str_out

for file in os.walk(path):
    for item in file[2]:
        os.rename(path+'\\'+item,path+'\\'+str_insert(item,12," "))
        os.rename(path+'\\'+item,path+'\\'+item.replace("+"," "))
print("Done!")
