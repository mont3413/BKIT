def print_result(func):
    def inner(*args):
        a = func(*args)
        print(func.__name__)
        if isinstance(a, dict):
            for key, value in a.items():
                print(key, " = ", value)
        elif isinstance(a, list):
            print(*a, sep='\n')
        else:
            print(a)
        return a
    return inner


@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    test_1()
    # test_2()
    # test_3()
    # test_4()
