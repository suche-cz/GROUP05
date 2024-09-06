# dt_test.py
import time
import datetime as dt

print('Hello')
print(time.time()) # počet sekund od 1.1.1970 tzv. Epoch
print(time.localtime())

t1 = time.time()
time.sleep(3)
t2 = time.time()
print(t2 - t1, 'rozdíl')

print(time.time())
print('Hello 2')
