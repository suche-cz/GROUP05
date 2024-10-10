# argumenty.py

def t(a, b, c, d, e, f):
    pass

def test(*args):
    print(args)


def t2(a=10, b=20, c=30, d=230, e=100):
    pass

def test2(**kwargs):
    a = kwargs['a']
    b = kwargs['b']

    if 'd' in kwargs:
        pass

test(1, 2, 3, 4, 5)
test2(a=10, b=20, c=30)

def xyz(*args, **kwargs):
    print
