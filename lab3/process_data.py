import json
from print_result import print_result
from unique import Unique
from gen_random import gen_random
from cm_timer import cm_timer_1

path = "/Users/mont/Desktop/data_light.json"

with open(path) as f:
    data = json.load(f)


#@print_result
def f1(arg):
    return sorted(Unique([vac["job-name"] for vac in arg]), key=lambda x: x.lower())


#@print_result
def f2(arg):
    return list(filter(lambda x: x[:11].lower() == "программист", arg))


#@print_result
def f3(arg):
    return list(map(lambda x: x + " с опытом Python", arg))


@print_result
def f4(arg):
    return [i[0] + ", зарплата " + str(i[1]) for i in list(zip(arg, gen_random(len(arg), 100000, 200000)))]


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
