# Exercise 7: Return the count of a given substring from a string
# str_x = str(input("Enter a sentence: ")).lower()
# word = str(input("Enter substring: "))

def count_emma(statement):
    print("Given String: ", statement)
    counts = 0
    for i in range(len(statement) - 1):
        counts += statement[i: i + 4] == 'Emma'
    return counts


count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
