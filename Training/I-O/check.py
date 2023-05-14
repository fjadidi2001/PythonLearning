# Exercise 9: Check file is empty or not
# with open('test.txt', 'r') as fp:
#     empty = fp.readlines()
#     for cou in empty:
#         if cou == 0:
#             print('file is empty')
#             break
#     print('file is not empty')


# another solution
# import os
#
# size = os.stat("text.txt").st_size
# if size == 0:
#     print('file is empty')


# another solution using try and except

# import os
#
# try:
#     if os.stat("new_file.txt").st_size == 0:
#         print('file is empty')
# except FileNotFoundError:
#     print('the specified file does Not exist')


# another solution

import os
if os.path.getsize('text.txt')==0:
    print('file is empty')
else:
    print('file is not empty')
