from string import ascii_lowercase as alc
from random import randrange as rr

letters = (ch*2 for ch in alc)

print(f'{letters = }')
print(f'{type(letters) = }\n')

print(f'{tuple(letters) = }\n')


scream = ''.join(ch*rr(2, 6) for ch in 'aoeu')
print(scream)
