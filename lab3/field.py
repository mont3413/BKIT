def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        arr = [d[args[0]] for d in items if args[0] in d]
        print(*arr, sep=", ")
    else:
        dict_arr = [{key: d[key] for key in args if key in d} for d in items]
        print(*dict_arr, sep=' ')


def main():
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
    ]
    field(goods, 'title')
    field(goods, 'title', 'price')


if __name__ == '__main__':
    main()
