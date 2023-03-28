seti0 = {"one", "two", "three"}
print(seti0)
# The values True and 1 are considered the same value in sets, and are treated as duplicates
seti1 = {"one", "two", "three",True,1}
print(seti1)
seti2 = {"one", "two", "three",False,0}
print(seti2)
