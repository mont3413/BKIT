from random import randint


def gen_random(num_count, begin, end):
    return [randint(begin, end) for i in range(num_count)]


def main():
    r = gen_random(5, 1, 3)
    print(*r)


if __name__ == '__main__':
    main()
