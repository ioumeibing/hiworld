def list():
    a = [2,5,66,77,11,45]
    #添加元素
    a.append(45)
    #在索引0位置添加元素1
    a.insert(0,1)
    #列表方法 count(s) 会返回列表元素中 s 的数量
    a.count(45)
    #在列表中移除任意指定值
    a.remove(66)
    #反转列表
    a.reverse()
    #将一个列表的所有元素添加到另一个列表的末尾
    b = [45,56,90]
    a.extend(b)
    #给列表排列
    a.sort()
    #del 关键字删除指定位置的列表元素
    del a[-1]
    print(a)
if __name__ == '__main__':
    list()
