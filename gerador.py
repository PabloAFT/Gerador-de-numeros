import time
a = 29943829
c = 12355
m = 2**32
origem = int(''.join(i for i in str(time.time()) if i.isdigit())[10:])
numbers = []
while len(numbers) != 6:
    origem = (a * origem + c) % m
    f_number = str(origem)[-2:]
    if f_number not in numbers and (int(f_number) < 61 and int(f_number) != 0):
        numbers.append(str(origem)[-2:])
print(numbers)
