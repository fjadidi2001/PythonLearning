# Method 1
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



# Method 2

s1 = "listen"
s2 = "silent"

if sorted(s1) == sorted(s2):
    print("Yes")
else:
    print("No")


# Method 3
def are_anagrams(str1, str2):
    """
    Checks if two strings are anagrams of each other.

    Args:
        str1: The first string.
        str2: The second string.

    Returns:
        True if the strings are anagrams, False otherwise.
    """
    # Convert strings to lowercase and remove spaces for case-insensitive and space-agnostic comparison
    s1_cleaned = str1.replace(" ", "").lower()
    s2_cleaned = str2.replace(" ", "").lower()

    # If the lengths are different after cleaning, they cannot be anagrams
    if len(s1_cleaned) != len(s2_cleaned):
        return False

    # Sort the characters of both cleaned strings and compare them
    return sorted(s1_cleaned) == sorted(s2_cleaned)

# Example Usage:
string1 = "Listen"
string2 = "Silent"
string3 = "Hello"
string4 = "World"
string5 = "A gentleman"
string6 = "Elegant man"

print(f"'{string1}' and '{string2}' are anagrams: {are_anagrams(string1, string2)}")
print(f"'{string3}' and '{string4}' are anagrams: {are_anagrams(string3, string4)}")
print(f"'{string5}' and '{string6}' are anagrams: {are_anagrams(string5, string6)}")