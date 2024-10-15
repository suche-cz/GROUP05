# test_file.py

# 'PY\\22\\test_file.txt'

with open('PY/22/test_file3.txt', mode='wb') as f:
    #f.write(b'+\xc4\x9b\xc5\xa1\xc4\x8d\xc5\x99\xc5\xbe\xc3\xbd\xc3\xa1\xc3\xad\xc3\xa9')
    f.write(b'\xc4\x9b')


exit()

with open('PY/22/test_file3.txt', mode='rb') as f:
    text = f.read()
    print(text)
    for item in text:
        print(item)

