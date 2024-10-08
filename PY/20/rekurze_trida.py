class Human:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent


a = Human('A', None)
b = Human('B', a)
c = Human('C', b)

def print_parents(obj):
    if obj.parent:
        print(obj.parent.name)
        print_parents(obj.parent)

print_parents(c)
