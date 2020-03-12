import random
from datetime import datetime

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

length = int(input('Длина пароля? '))

password =''

start = datetime.now() 

for i in range(length):
    password += random.choice(chars)

end = datetime.now()
total = end - start

print(password)
print(f"Пароль создан за {str(total)} секунд, длина пароля {len(password)} символов")