# Atbash Cipher
# Hanya utnuk huruf besar

def getMode():
    while True:
        print('Apa yang ingin anda lakukan')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Masukan "encrypt" atau "e" atau "decrypt" atau "d".')

def getMessage():
    return input('Masukan pesan: ')

def getTranslatedMessage(mode, message):
    translated = ''
    for symbol in message:
        num = ord(symbol)
        num -= ord('A')
        num = -(num + 1) % 26
        num += ord('A')
        translated += chr(num)
    return translated

mode = getMode()
message = getMessage()

print('Hasil: ', getTranslatedMessage(mode, message))

