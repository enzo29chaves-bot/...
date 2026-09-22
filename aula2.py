import random
elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
q1 = int(input("fale a quantidade de caracteres da sua senha"))
code = ""
for i in range(q1):
    code += random.choice (elements)


print (code)
