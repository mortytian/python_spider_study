def get_peach(n):
    number = 1
    day = 10
    while day != 1:
        day -= 1
        number += 1
        number *= 2
    return number

number = 1
for i in range(1,10):
    number += 1
    number *= 2


print(get_peach())
print(number)
