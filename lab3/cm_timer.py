import time
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self, time1=0, time2=0):
        self.time1 = time1
        self.time2 = time2

    def __enter__(self):
        self.time1 = time.time()

    def __exit__(self, exp_type, exp_value, traceback):
        if exp_type is not None:
            print(exp_type, exp_value, traceback)
        else:
            self.time2 = time.time()
            print("time:", self.time2 - self.time1)


@contextmanager
def cm_timer_2():
    time1 = time.time()
    yield
    time2 = time.time()
    print("time:", time2 - time1)


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)

    with cm_timer_2():
        time.sleep(3.0)

