import os
import shutil
#批量移动文件夹
path = "F:\会计专硕3班\QQ邮箱"
file_folder=os.walk(path)
for i in file_folder:
    if i[0]==path:
        continue
    else:
        for file in i[2:][0]:
            shutil.copy(i[0] +"\\" + file,path)
print("Done!")