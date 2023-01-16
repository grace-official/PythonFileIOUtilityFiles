from FileRead import FileRead
from FileWrite import FileWrite
from FileEncrypter import FileEncrypter
from FileDecrypter import FileDecrypter

reader = FileRead()
writer = FileWrite()
encrypt = FileEncrypter()

# 1. ASCII values and casting
# Cesarean Cipher

"""
letter = 'a'
num = ord(letter)
print(num)
newLetter = chr(num + 1)
print(newLetter)
"""

# 2. How to change the characters in a string

word = 'Hello'

wordData = list(word)
print(wordData)

# 3. Basic encryption


