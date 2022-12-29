class Unique(object):
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        if kwargs=={}:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs["ignore_case"]
        self.num = -1
        self.items=items

    def __next__(self):
        if self.num == len(self.items)-1:
            raise StopIteration
        self.num += 1
        if isinstance(self.items[self.num], str):
            if not self.ignore_case:
                if self.items[self.num] in self.items[:self.num]:
                    next(self)
            else:
                for i in self.items[:self.num]:
                    if i.lower() == self.items[self.num].lower():
                        next(self)
        else:
            if self.items[self.num] in self.items[:self.num]:
                next(self)
        return self.items[self.num]

    def __iter__(self):
        return self


def main():
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for i in Unique(data, ignore_case=True):
        print(i)


if __name__ == '__main__':
    main()
