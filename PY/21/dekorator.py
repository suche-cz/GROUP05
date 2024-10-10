# dekorator.py
# decorate = ozdobit

from functools import lru_cache

@lru_cache
def test1():
    print('work 1')
    return 1 + 1

@lru_cache
def test2():
    print('work 2')
    return 2 + 1

print('>>>>>>>', __name__)

if __name__ == '__main__':
    # tato část kodu se spustí pouze, když se pustí tento soubor
    # pokud je tento soubor importovaný tak se toto neprovede

    def main():
        a = 10
        print(test1())
        print(test1())
        print(test2())
        print(test2())
    
    main()



