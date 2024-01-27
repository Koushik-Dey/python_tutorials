def encode(code):
    char = "@123"
    if (len(code) >= 3):
        encodedValue = code[1:] + code[0] + char
        return encodedValue
    else:
        return code

# print(encode("hitesh"))


def decode(code):
    if (len(code) >= 3):
        removeLastChar = code[:-4]
        return removeLastChar[-2:-1] + removeLastChar[:-1]
    else:
        return code


print(decode(encode("koushik")))
