str = input('输入一段话：')
str1 = str[::-1]
if str == str1:
    print("是回文")
else:
    print("不是回文")