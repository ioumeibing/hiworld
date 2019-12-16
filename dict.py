def dict():
    data = {'kushal': 'Fedora', 'kart_': 'Debian', 'Jace': 'Mac'}
    #使用 del 关键字删除任意指定的键值对：
    del data['kushal']
    #使用 in 关键字查询指定的键是否存在于字典中。
    'ShiYanLou' in data

    #字典中的键必须是不可变类型，比如你不能使用列表作为键

    #dict() 可以从包含键值对的元组中创建字典。
     #dict((('Indian', 'Delhi'), ('Bangladesh', 'Dhaka')))
    #{'Indian': 'Delhi', 'Bangladesh': 'Dhaka'}

    #遍历一个字典，使用字典的 items() 方法
    for x, y in data.items():
        print("{} user {}".format(x, y))

    #往字典中的元素添加数据，我们首先要判断这个元素是否存在，不存在则创建一个默认值
    datas = {}
    datas.setdefault('name', []).append('Ruby')
    datas.setdefault('name', []).append('python')
    print(datas)


if __name__ == '__main__':
    dict()
