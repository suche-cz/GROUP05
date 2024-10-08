"""
!0 = 1
!1 = 1
!2 = 1 * 2
!3 = 1 * 2 * 3
!4 = 1 * 2 * 3 * 4
!5 = 1 * 2 * 3 * 4 * 5

!0 = 1
!1 = 1
!2 = !1 * 2 = 2
!3 = !2 * 3 = 6
!4 = !3 * 4 = 24
!5 = !4 * 5 = 120

!n = !(n-1) * n
"""

def factorial(n: int):
    if n < 0:
        raise ValueError('Faktorial nelze počítat pro záporná čísla')
    if n == 2:
        return 2
    if n < 2:
        return 1

    vysledek = factorial(n-1) * n
    return vysledek

"""
1
5
5 * 4 = 20
20 * 3 = 60
60 * 2 = 120
"""
def factorial_loop(n):
    result = 1
    while n > 1:
        result = result * n
        n = n - 1
    
    return result


print(factorial(5))
print(factorial(10))
print(factorial_loop(5))
print(factorial_loop(10))

def test_rekurze():
    factorial(100)

def test_loop():
    factorial_loop(100)

import timeit

print(timeit.timeit(test_rekurze, number=100_000))
print(timeit.timeit(test_loop, number=100_000))


