from bs4 import BeautifulSoup
import  time
'''
函数：
1、无参，无返回类型：
def 函数名（）
    函数主体

2、无参，有返回类型

3、有参，无返回

4、有参，有返回

函数的调用

缺省参数

lambda
sum = lambda a,b:a+b
'''

'''
如何修改全局变量的值：
 加上global

'''

def cal(n):
    if n == 1:
        return 1
    else:
        return cal(n-1) * n

def cal1(n):
    a = 1
    sum = 1
    while a <= n:
        sum *= a
        a += 1
    return sum

x = 90

start = time.time()
cal(x)
end =  time.time()
print(round((end - start),5))

start = time.time()
cal1(x)
end = time.time()
print(round((end - start),5))

def cal(a,b,opt):
    print(opt(a,b))

a = 1
b = 2
sum = lambda a,b : a+b

cal(a,b,sum)

students = [{'name' : 'zh', 'age' : 25},
            {'name' : 'ch', 'age' : 14},
            {'name' : 'fj', 'age' : 16}]


students.sort(key = lambda a : a['name'])
print(students)