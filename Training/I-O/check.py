# Exercise 9: Check file is empty or not
with open('test.txt', 'r') as fp:
    empty = fp.readlines()
    for cou in empty:
        if cou == 0:
            print('file is empty')
            break
    print('file is not empty')

