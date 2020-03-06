'''
异常操作:
    当python解释遇到错误，无法继续执行,提示错误信息 称为异常
    try...except
    try:可能发生异常的代码
    except:对异常进行处理，只有发生异常时except才会执行
开发中可以捕获多个异常
    try...except...finally..

异常对传递：
    产生异常处不不处理，由调用方处理

自定义异常：
    1、选择一个异常类继承
    2、使用raise语句抛出一个异常实例

'''

class MyError(ValueError):
    print(ValueError)

def f(n):
    if n == 0:
        raise MyError('n不能为0')
    return 10/n
result = f(0)
print(result)