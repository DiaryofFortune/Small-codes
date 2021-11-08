'''应用场景:
有些时候，就算命名格式写的非常清楚了，收到的文件命名也是五花八门。
'''
import os
import re
#如果想要在文件名中的xx位置插入xx分隔符，如将“20211108张三.docx”修改为“20211108 张三.docx”，则可以用到下面这个方法
def str_insert(str_origin,pos,str_add):
    str_list=list(str_origin)
    str_list.insert(pos,str_add)
    str_out=''.join(str_list)
    #这里不能直接返回str_list，因为str_list是list类不是str类，所以需要用join函数将分割后的list还原为str
    return str_out

if __name__=='__main__':
    path='F:\xx专业xx班\期末作业'
    for file in os.walk(path):
        for item in file[2]:
        #这里的file[2]是由os.walk函数决定的，因为所有要处理的文件都在一个目录下，故file元组的file[0]是path，file[1]为空，所以要跳过file的前两项
            os.rename(path+'\\'+item,path+'\\'+str_insert(item,12," "))
            #插入分隔符和替换文件名
            os.rename(path+'\\'+item,path+'\\'+item.replace("+"," "))
            #上面这两行代码不能同时执行，同时执行会显示找不到文件（因为文件名已被处理）
    print("Done!")
