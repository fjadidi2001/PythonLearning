# Exercise 9: Check Palindrome string

s = input('enter string: ')


def palindrome( string):
    x = ""
    for i in string:
        x = i + x
    return x


if s == palindrome(s):
    print('its a palindrome')
else:
    print('its not a palindrome')
