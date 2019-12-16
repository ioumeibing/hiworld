def set():
    # 集合是一个无序不重复元素的集
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    #想要创建空集合，你必须使用 set()
    #pop 方法随机删除一个元素并打印
    basket.pop()
    #添加元素
    basket.add('sdfd')
    print(basket)


if __name__ == '__main__':
    set()

