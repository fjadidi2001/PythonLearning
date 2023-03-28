seti0 = {"one", "two", "three"}
print(seti0)
# The values True and 1 are considered the same value in sets, and are treated as duplicates
seti1 = {"one", "two", "three", True, 1}
print(seti1)
seti2 = {"one", "two", "three", False, 0}
print(seti2, len(seti2))
seti3 = set(("hi", "hello", "cherry"))
for i in seti3:
    print(i)
# check item in a list
print("hi" in seti3)
seti3.add('but')
for i in seti3:
    print(i)
seti3.update(seti2)
print(seti3)
listi = ["ha", "joker"]
seti2.update(listi)
print(seti2)
