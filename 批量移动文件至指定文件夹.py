'''应用场景描述：
客户在一个文件夹A里面存放了B,C,D文件夹和b,c,d,e,f,g文件，在B,C,D文件夹下又有h,i,j,k文件。
我想将h,i,j,k文件移动至A文件夹下，以便统一批量管理。
'''
#python基本库就可以
import os
import shutil
#首先确定文件夹A的路径
path = "F:\user"
#用os.walk遍历，os.walk会一个一个打开文件夹并返回文件夹下的文件名
file_folder=os.walk(path)
for i in file_folder:
    if i[0]==path:
    #我不想对A文件夹下的文件进行任何操作，所以需要跳过
        continue
    else:
        for file in i[2:][0]:
            shutil.copy(i[0] +"\\" + file,path)
print("Done!")
