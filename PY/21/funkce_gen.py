# funkce_gen.py
def create_operation(multiply):
    def operation(a, b):
        return (a + b) * multiply

    return operation


a = create_operation(10)
b = create_operation(100)

print(a == b)
print(a is b)

print(a)
print(a(1, 2))
print(b(1, 2))
