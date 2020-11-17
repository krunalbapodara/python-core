with open("test.txt", 'w+') as f:
    f.write('Hello world,\nI am krunal')

with open("test.txt", 'r') as f:
    print(f.read())
    print(f.tell())
    f.seek(0)
    print(f.tell())
