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
seti2.remove("one")
# Note: If the item to remove does not exist, remove() will raise an error.
print(seti2)
seti2.discard("one")
# Note: If the item to remove does not exist, discard() will NOT raise an error.
print(seti2)
# pop
f = seti2.pop()
print(f)
print(seti2)
seti1.clear()
print(seti1)
del seti0

print("===============================")
se1 = {"fati", "jadidi", True, 7.58}
se2 = set(("zi", "jadidi", False, 10.2))
se3 = se1.union(se2)
print(se3)
se1.intersection_update(se2)
print(se1)