def caesarCipherEncryptor(string, key):
    # Write your code here.
    char_to_int = {}

    for i in range(97, 97+26):
        char_to_int[chr(i)] = i - 97

    chars = list(char_to_int.keys())

    result = ""

    for i, c in enumerate(string):
          k = char_to_int[c] + key
          k = k%26
          result = result + chars[k]

    return result


print (caesarCipherEncryptor("xyz", 2))
