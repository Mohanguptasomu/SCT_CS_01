
# ENCRYPTION & DECRYPTION

letters= 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

#Encryption
def encrypt(plaintext,key):
    ciphertext= ''
    for letter in plaintext:
        letter = letter.lower()
        if not letter =='  ':
            index = letters.find(letter)
            if index == -1:
                ciphertext += letter
            else:
                new_index= index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                ciphertext += letters[new_index]
    return ciphertext


# Decryption
def decrypt(ciphertext,key):
    plaintext= ''
    for letter in ciphertext:
        letter = letter.lower()
        if not letter == '  ':
            index = letters.find(letter)
            if index == -1:
                plaintext += letter
            else:
                new_index= index - key
                if new_index < 0:
                    new_index +=  num_letters
                plaintext += letters[new_index]
    return plaintext

print()
print('***CASER CIPHER PROGRAM***')
print()

print('Do you want to encrypt or decrypt or decrypt?')
user_input = input('e/d: ').lower()
print()


#Encryption and decryption ststements
if user_input =='e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text =input('Enter the text to encrypt:')
    ciphertext = encrypt(text, key)
    print(f'CIPHERTEXT :{ciphertext}')

elif user_input =='d':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26):'))
    text =input('Enter the text to decrypt:')
    plaintext= decrypt(text, key)
    print(f'plainTEXT :{plaintext}')