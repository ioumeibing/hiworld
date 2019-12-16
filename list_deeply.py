def list1():
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    # 等价于squares = [x**2 for x in range(10)]


def list2():
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    # 等价于[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]


def list3():
    a = [1, 2, 3]
    z = []
    for x in [x ** 2 for x in a]:
        z.append(x + 1)
    print(z)
    # 等价于 z = [x + 1 for x in [x ** 2 for x in a]]


if __name__ == '__main__':
    list3()

