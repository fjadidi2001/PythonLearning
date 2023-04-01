# Exercise 7: Return the count of a given substring from a string
str_x = "Emma is good developer. Emma is a writer"
# use count method of a str class
cnt = str_x.count("Emma")
print(cnt)
#

def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count


count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")
