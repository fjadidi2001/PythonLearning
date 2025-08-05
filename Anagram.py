from collections import Counter  # for character frequency counting

s1 = "listen"
s2 = "silent"

if len(s1) != len(s2):  # check length
    print("No")
else:
    if Counter(s1) == Counter(s2):  # compare character counts
        print("Yes")
    else:
        print("No")





s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Yes")
else:
    print("No")