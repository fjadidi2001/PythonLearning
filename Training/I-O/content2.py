with open('test.txt', 'r') as fp:
    lines = fp.readlines()
with open('new_file2.txt', 'w') as fp:
    COUNT = 0
    for line in lines:
        if COUNT == 3:
            COUNT += 1
            continue
        else:
            fp.write(line)
        COUNT += 1
