import os
import shutil
"""
访问模式：
r:只读
w:写入，覆盖原文件
a：追加

rb:二进制只读
rw
ra

r+:打开一个文件用于读写。文件指针将会放在文件的开头。
w+:打开一个文件用于读写。
    如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。
    如果该文件不存在，创建新文件。

a+:读写 指针放末尾 追加



文件读写操作
1、写入: write
2、读出: read read(n) 读取 n 个 默认全部读取
3、readlines: 读取全部行
"""


"""
文件重命名
    os中rename
    os.rename(originname, newname)
    
文件删除 
    os中remove
   
创建文件夹
    os.mkdir(name)

删除文件夹
    os.rmdir(name)
    
创建多级文件夹
    os.makedirs(path)
    
获取当前目录
    os.getcwd()
    
删除文件夹
    os.rmdir()
    
删除多级文件夹
    shutil模块中的rmtree()
   
移动文件夹
    shutil.move(originpath,newpath) 
    
复制文件
    shutil.copyfile(origin path and name, new path and name)
"""
# 对原有文件进行备份


# filename = input('输入文件名: ')
# filename = 'test.txt'
# name = filename.split('.')[0]
# tag =  filename.split('.')[1]
# newfile = name + '附件.' + tag
# with open(filename, 'r') as r:
#     with open(newfile, 'w') as w:
#         line = r.readline()
#         while len(line) != 0:
#             w.write(line)
#             line = r.readline()
#
# os.rename('case.txt','test.txt')

# os.remove('test附件.txt')


'''
编写分页显示文本的程序
输入文件名 默认显示10行
继续阅读 下面10行
否则 结束
'''

# filename = input('输入文件名')
filename = 'test.txt'
with open(filename, 'r') as r:
    flag = 1
    line = r.readline()
    while len(line) != 0:
        print(line,end = '')
        flag += 1
        line = r.readline()
        if flag == 10:
            p = input('继续 y/n: ')
            if p == 'n':
                break
            else:
                flag = 0
