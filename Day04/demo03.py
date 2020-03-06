'''
模块：
    1、模块的使用
        import:导入某个模块，如果有多个模块 用逗号分隔
            import module1,module2..
        使用模块中的某个函数时： 模块名.函数名的方式。
        from ... import ...

    2、模块的制作
        在python中，每一个python文件都可以作为一个模块
        模块的名字就是文件的名字
        __all__=["module_a","module_b"]
在使用 from package_name import * 时 ,
表示import 该package 中的 两个module及 两个module相关的类、方法等。
'''

# import text