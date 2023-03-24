mess = input(">")
words = mess.split(' ')
emojis = {
    ":)": ":|",
    ":(": ":| "
}
out = ""
for word in words:
    out += emojis.get(word, word) + " "
print(out)
