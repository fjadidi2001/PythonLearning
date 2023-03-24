def emoji_converter(mess):
    words = mess.split(' ')
    emojis = {
        ":)": ":|",
        ":(": ":| "
    }
    out = ""
    for word in words:
        out += emojis.get(word, word) + " "
    return out


mess = input(">")
print(emoji_converter(mess))
