import  random
mystr = 'hello my friends and myself'

'''
find: 
可以指定开始位置 默认为0 
检查str是否存在与mystr中
存在返回从开始位置开始最先出现的下表
不存在返回-1

mystr.find(str,start = 0, end = len(mystr))
'''

'''
find: 
可以指定开始位置 默认为0 
检查str是否存在与mystr中
存在返回从开始位置开始最先出现的下表
不存在 抛出异常

mystr.index(str,start = 0, end = len(mystr))

'''

'''
count:
检查str在mystr中存在的次数，也可以指定查找区间，
默认strat = 0, end = length.
mystr.count(str, start = 0, end = len(mystr))

'''

'''
replace
把mystr中的str1替换为str2，如果count指定则替换count次
mystr.replace(str1,str2,mystr.count(str1))

'''


''''
split
以str为分隔符，切片mystr,返回一个列表
newStr = mystr.split(str,maxsplit)
'''

'''
capitalize
把字符串的第一个字符大写
mystr.capitalize()
'''

'''
title
把字符串中每一个单词首字母大写
mystr.title()
'''

'''
startswith
检查字符串是否以str开头
是的话返回True 否则False
mystr.startswith(str)
'''
'''
endswith
检查字符串是否以str结尾
mysrt.endswith(str)
'''

'''
lower
把mystr中所有的大写字母变成小写
mystr.lower()
'''

'''
upper
把mystr中所有的小写字母变成大写
mystr.upper()
'''

'''
strip
去掉mysrt中首位的空格去掉
mystr.strip()

lstrip()
rstrip()
只去除左边或者右边的空格
'''

'''
splitlines
按照行进行分隔，返回一个包含各行作为元素的列表
mystr.splitlines()
'''

'''
isalpha
判断mystr中所有的字符是不是字母
是返回True
mystr.isalpha()
'''

'''
isdigit
判断字符串中是不是只有数字
'''

'''
isalnum
如果mystr中只有数字和字母
则返回True
mystr.isalnum()
'''

'''
isspace
判断mystr中是否只有空格
是则返回True
mystr.isspace()
'''

''''
join
把mystr插入到str的每个字符前，构造出一个新的字符串
mystr.join(str)
'''

'''
列表：存储一组数据，不固定数据类型
'''

'''
列表相关操作
append 追加
mylist.append(object)
object作为一个整体添加进去

extend
mylist.append(iterable)
追加一个可迭代对象

insert
在指定位置之前插入元素
mylist.insert(index,object)

'''

'''
修改元素
采用赋值的方式修改列表元素


查找元素
in 判断element是否在列表中
notin 相反
index 查看列表中元素的位置
count 查看列表中元素存在的次数

删除元素：(del, pop, remove)
del:根据下标进行删除
pop:删除最后一个元素
remove:根据元素的值进行删除

排序操作: (sort, reverse)
sort:默认从小到大排序，reverse参数默认为False
    如果需要从大到小排序，设置reverse
   
reverse
反转列表 
'''

'''
元组:
元组支持下标操作
元组中元素的值不能改变，也不能删除
'''

'''
字典：
存储多条数据
字典中的每条数据由两部分组成，key和value
get(key, default value(:
    避免由于key不存在导致的查询错误
    当key不存在当时候，返回默认值
    key存在的时候，返回具体指
    
修改字典元素:
    注意当key存在当时候通过赋值的方式可以修改
    当key不存在的时候，则增加元素
    
删除元素: del,clear()
    del:删除指定元素 del info['name']
        删除整个字典 del info
    clear:清空字典

字典中的常见操作：
    1.len:获取字典的长度
    2.keys:返回一个列表，包含字典中所有的key可遍历，但不支持索引
    3.values:返回一个列表，包含字典中的所有value可遍历，但不支持索引
    4.items:返回一个包含键值对的列表，可遍历，不支持索引
        
'''

str = 'my'
print(mystr.find(str))

print(mystr.find(str,7))

str1 = 'sf'
print(mystr.find(str1))

mylist = [1,2,3]
list2 = [2,3,4]

mylist.insert(0,[1,2])

lists = ['a','b','c']
namelist = ['e','f','g','a']

namelist.sort()

print(namelist)
print( 'e' in namelist)

schoolnames = [['北大', '清华'],
               ['南开', '天大', '师范']]

for items in schoolnames:
    for item in items:
        print(item, end = ' ')
    print()

length = len(schoolnames)
for i in range(length):
    lists = schoolnames.pop()
    for j in lists:
        print(j, end = ' ')
    print()

room_number = 3
teacher_number = 8

room = [[], [], []]
teacher = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for tea in teacher:
    room_number = random.randint(0,2)
    room[room_number].append(tea)
print(room)