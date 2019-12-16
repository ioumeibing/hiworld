def tuple():
    a = ('Fedora', 'ShiYanLou', 'Kubuntu', "Pardus")
    for x in a:
        print(x, end=" ")
    # 可以对任何一个元组执行拆封操作并赋值给多个变量
    x, y, z, b = a = ('Fedora', 'ShiYanLou', 'Kubuntu', "Pardus")
    print(x+y+z+b)
    #元组是不可变类型，这意味着你不能在元组内删除或添加或编辑任何值

    #要创建只含有一个元素的元组，在值后面跟一个逗号
    a = (123,)


if __name__ == '__main__':
    tuple()

