# Caesar Cipher

def getMode():
    while True:
        print('Apa yang ingin anda lakukan')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Masukan "encrypt" atau "e" atau "decrypt" atau "d".')

def getMessage():
    print('Masukan plainteks:')
    return input()

def getKey():
    key = 0
    while True:
        print('Masukan key: ')
        key = int(input())
        return key % 26

def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated

print('ini adalah kriptografi menggunakan ROT13')
mode = getMode()
message = getMessage()
key = 13

print('Your translated text is:')
print(getTranslatedMessage(mode, message, key))
